class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_tank_error() -> None:
    raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as error:
        print("Caught PlantError:", error)

    print("\nTesting WaterError...")
    try:
        water_tank_error()
    except WaterError as error:
        print("Caught WaterError:", error)

    print("\nTesting catching all garden errors...")
    for action in (plant_error, water_tank_error):
        try:
            action()
        except GardenError as error:
            print("Caught a garden error:", error)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
