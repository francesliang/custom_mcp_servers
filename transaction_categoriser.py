from typing import Any
from mcp.server.fastmcp import FastMCP
import mcp.types as types


EXPENSE_CATEGORIES = [
    "Food/drinks",
    "Gifts",
    "Health/medical",
    "Home",
    "Transportation",
    "Personal",
    "Pets",
    "Utilities",
    "Travel",
    "Mortgage",
    "Weekly household",
    "Clothing",
    "Beauty",
    "Investment property"
]

INCOME_CATEGORIES = [
    "Paycheck",
    "Rental income",
    "Other"
]


# Initialize FastMCP server
mcp_server = FastMCP("transaction-categoriser-server")


@mcp_server.prompt()
async def categorise_transactions(
    transaction_folder: str
) -> list[types.PromptMessage]:
    return [
        types.PromptMessage(
            role="user",
            content=types.TextContent(
                type="text",
                text=f"Read the transaction files from {transaction_folder}"
            ),
        ),
        types.PromptMessage(
            role="user",
            content=types.TextContent(
                type="text",
                text=f"""
                Extract the expense transactions, and categorise them into these categories: {EXPENSE_CATEGORIES}. 
                Then output the final expense transactions into format 'Date, Amount, Description, Category' in csv format
                """
            ),
        ),
        types.PromptMessage(
            role="user",
            content=types.TextContent(
                type="text",
                text=f"""
                Extract the income transactions, and categorise them into these categories: {INCOME_CATEGORIES}. 
                Then output the final income transactions into format 'Date, Amount, Description, Category' in csv format
                """
            ),
        ),
    ]


if __name__ == "__main__":
    # Initialize and run the server
    mcp_server.run(transport='stdio')