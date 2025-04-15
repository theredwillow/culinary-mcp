## General
- Does MCP have versioning?
- Add bar code / SKU system, read grocery store receipts, etc...
- Add error handling for Python file operations
- Create model-specific localization files

## Config
- Record user preferences like allergies and diet information

## Meal plans
- On add: should add ingredients to shopping list?
- Add meal plan prompt
- Record meal suggestions and, if provided, whether the user liked them

## Shopping lists
- Currently checks for exact string, ask LLM for synonyms (e.g. garbanzo beans and chickpeas)
- Connect to grocery store API('s) to add aisle numbers

## Recipe book
- Design a recipe storing system
- Add plan meal function, adding to shopping list (new data: plans for ingredient)