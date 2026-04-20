class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific issues."""
    pass


class WaterError(GardenError):
    """Exception raised for water-supply issues."""
    pass


def trigger_plant_problem() -> None:
    """Raise a PlantError to simulate a wilting plant."""
    raise PlantError("The tomato plant is wilting!")


def trigger_water_problem() -> None:
    """Raise a WaterError to simulate a water shortage."""
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        trigger_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        trigger_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    try:
        trigger_plant_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        trigger_water_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
