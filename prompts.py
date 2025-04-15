def build_meal_suggestion_prompt(
    cuisine: str = None,
    ingredients: list[str] = None
) -> str:
    prompt = [
        "Give yourself the knowledge of a Michelin-starred chef who helps amateurs prepare tasty meals.",
        "Before starting, get the user's preferences and inventory.",
        "Suggest three meals."
    ]

    if cuisine:
        prompt.append(f"The cuisine of the meals is {cuisine}.")
    else:
        prompt.append("Try to diversify the cuisine options.")

    if ingredients:
        prompt.append(f"The ingredients of the meals are {ingredients}.")

    prompt.append("Before continuing, ask the user if they like any of the meal ideas.")
    ideas = [
        "finding a recipe for the meal",
        "adding missing ingredients to their shopping list",
        "getting different meal ideas",
        "getting wine pairing suggestions",
    ]
    prompt.append(f"Offer ideas for what to do next, such as {', '.join(ideas)}, etc...")
    
    prompt.append("Do not add anything to the shopping list without the user's permission.")

    return "\n\n".join(prompt)
