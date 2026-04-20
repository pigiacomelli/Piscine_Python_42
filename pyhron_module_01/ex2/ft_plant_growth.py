class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_one_day()
        plant.show()

    growth = round(plant.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()