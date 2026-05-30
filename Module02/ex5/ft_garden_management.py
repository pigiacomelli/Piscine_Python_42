class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class TankError(GardenError):
    pass


class WaterError(GardenError):
    pass


class HealthCheckError(GardenError):
    pass


class GardenManager:
    MAX_TANK: int = 10

    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}
        self.water_tank: int = 5

    def add_plant(self, name, water, sun) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")

        if name in self.plants:
            raise PlantError(f"The plant '{name}' already exists!")

        self.plants[name] = {
            "water": water,
            "sun": sun
        }
        print(f"Added {name} successfully")

    def fill_tank(self, amount) -> None:
        if amount <= 0:
            raise TankError("Fill amount must be positive")

        if self.water_tank + amount > self.MAX_TANK:
            raise TankError("Tank is already full")

        self.water_tank += amount
        print(f"Tank filled. Current water level: {self.water_tank}")

    def water_plants(self) -> None:
        if self.water_tank <= 0:
            raise WaterError("Not enough water in tank")

        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")

                self.plants[plant]["water"] += 1
                self.water_tank -= 1
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name) -> None:
        if name not in self.plants:
            raise HealthCheckError(f"Plant {name} not found")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise HealthCheckError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise HealthCheckError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise HealthCheckError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise HealthCheckError(
                f"Sunlight hours {sun} is too high (max 12)"
                                   )

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def main() -> None:
    print("=== Garden Management System ===\n")

    manager: GardenManager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 4, 8)
        manager.add_plant("lettuce", 14, 8)
        manager.add_plant("", 3, 6)
    except PlantError as error:
        print(f"Error adding plant: {error}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as error:
        print(f"Error watering plants: {error}")

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato")
        manager.check_plant_health("lettuce")
    except HealthCheckError as error:
        print(f"Error checking lettuce: {error}")

    print("\nTesting error recovery...")
    try:
        manager.water_tank = 0
        manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
