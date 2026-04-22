class PlantError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    # Check if name is capitalized correctly
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    # ---- Valid plants ----
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print()
    # ---- Invalid plants ----
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for plant in ["Tomato", "lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()