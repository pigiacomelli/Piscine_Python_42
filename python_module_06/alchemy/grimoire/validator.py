def validate_ingredients(ingredients: str) -> str:
    if "fire" in ingredients or "air" in ingredients:
        return f"{ingredients} - VALID"
    elif "water" in ingredients or "earth" in ingredients:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"