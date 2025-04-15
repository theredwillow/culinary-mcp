# mcp.py

from fastmcp import FastMCP
from mcp.server.fastmcp.prompts import Prompt
from mcp.server.fastmcp.prompts.base import PromptArgument
from utils import get_list, add_to_list, remove_from_list, check_for_item
from prompts import build_meal_suggestion_prompt

mcp = FastMCP("Chef Consultant 👨‍🍳")

# MEAL PLAN TOOLS
meal_suggestion_prompt = Prompt(
    name="suggest-a-meal",
    description="Suggest a meal, taking into account the user's preferences",
    arguments=[
        PromptArgument(
            name="cuisine",
            description="The cuisine of the meal",
            required=False,
        ),
        PromptArgument(
            name="ingredients",
            description="Ingredients that must be used in the meal",
            required=False,
        ),
    ],
    fn=build_meal_suggestion_prompt,
)
mcp.add_prompt(meal_suggestion_prompt)


@mcp.tool()
def get_preferences() -> str:
    """Get the user's preferences"""
    return get_list("preferences")


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
def add_multiple_items_to_shopping_list(items: list[str]) -> str:
    """Add multiple items to the shopping list"""
    return {item: add_item_to_shopping_list(item) for item in items}


@mcp.tool()
def remove_item_from_shopping_list(item: str) -> str:
    """Remove an item from the shopping list"""
    remove_from_list("shopping-list", item)
    return "Removed."


@mcp.tool()
def remove_multiple_items_from_shopping_list(items: list[str]) -> str:
    """Remove multiple items from the shopping list"""
    return {item: remove_item_from_shopping_list(item) for item in items}


# MULTIPLE DOMAIN TOOLS


@mcp.tool()
def check_for_item_in_either_list(item: str) -> str:
    """Check if an item is in the inventory or shopping list"""
    if check_for_item("inventory", item):
        return "In inventory."
    if check_for_item("shopping-list", item):
        return "In shopping list."
    return "Not found."

@mcp.tool()
def check_for_multiple_items_in_either_list(items: list[str]) -> str:
    """Check if multiple items are in the inventory or shopping list"""
    return {item: check_for_item_in_either_list(item) for item in items}
