def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int
                       ) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n"
            )
    if sunlight_hours > 12:
        raise ValueError(
             f"Sunlight hours {sunlight_hours} is too high (max 12)\n"
             )

    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 8, 4))
    except ValueError as error:
        print("Error:", error)

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(None, 8, 4))
    except ValueError as error:
        print("Error:", error)

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 4))
    except ValueError as error:
        print("Error:", error)

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 8, 0))
    except ValueError as error:
        print("Error:", error)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
