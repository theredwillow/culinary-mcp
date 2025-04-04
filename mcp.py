# mcp.py

from fastmcp import FastMCP
from utils import get_list, add_to_list, remove_from_list, check_for_item

mcp = FastMCP("Chef Consultant 👨‍🍳")

# INVENTORY TOOLS


@mcp.tool()
def get_inventory() -> str:
    """Get the inventory as a comma-separated list, such as fridge, pantry, cabinet, etc..."""
    return get_list("inventory")


@mcp.tool()
def add_item_to_inventory(item: str) -> str:
    """Add an item to the inventory, such as fridge, pantry, cabinet, etc..."""
    add_to_list("inventory", item)
    return "Added."


@mcp.tool()
def remove_item_from_inventory(item: str) -> str:
    """Remove an item from the inventory, such as fridge, pantry, cabinet, etc..."""
    remove_from_list("inventory", item)
    return "Removed."


# SHOPPING LIST TOOLS


@mcp.tool()
def get_shopping_list() -> str:
    """Get the shopping list as a comma-separated list"""
    return get_list("shopping-list")


@mcp.tool()
def add_item_to_shopping_list(item: str, force: bool = False) -> str:
    """Add item to shopping list."""
    if not force:
        if check_for_item("shopping-list", item):
            return (
                "Already in shopping list. Call again with force=True to add duplicate."
            )
        if check_for_item("inventory", item):
            return "Already in inventory. Call again with force=True to add anyway."

    add_to_list("shopping-list", item)
    return "Added."


@mcp.tool()
def remove_item_from_shopping_list(item: str) -> str:
    """Remove an item from the shopping list"""
    remove_from_list("shopping-list", item)
    return "Removed."


# MULTIPLE DOMAIN TOOLS


@mcp.tool()
def check_for_item_in_either_list(item: str) -> str:
    """Check if an item is in the inventory or shopping list"""
    if check_for_item("inventory", item):
        return "In inventory."
    if check_for_item("shopping-list", item):
        return "In shopping list."
    return "Not found."
