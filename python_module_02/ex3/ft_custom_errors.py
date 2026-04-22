class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


# Functions that raise custom errors
def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    # Test PlantError
    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    # Test WaterError
    try:
        print("Testing WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    # Catch all garden-related errors
    print("Testing catching all garden errors...")
    for func in (check_plant, check_water):
        try:
            func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()