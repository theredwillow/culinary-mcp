# mcp.py

from fastmcp import FastMCP
from utils import get_list, add_to_list, remove_from_list

mcp = FastMCP("Chef Consultant 👨‍🍳", dependencies=["utils"])

# INVENTORY TOOLS

@mcp.tool()
def get_inventory() -> list:
    """Get the inventory as a comma-separated list, such as fridge, pantry, cabinet, etc..."""
    return get_list("inventory")


@mcp.tool()
def add_item_to_inventory(item: str) -> None:
    """Add an item to the inventory, such as fridge, pantry, cabinet, etc..."""
    return add_to_list("inventory", item)


@mcp.tool()
def remove_item_from_inventory(item: str) -> None:
    """Remove an item from the inventory, such as fridge, pantry, cabinet, etc..."""
    return remove_from_list("inventory", item)
