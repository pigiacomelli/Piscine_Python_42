class Plant:
    """
    Represents a plant with name, height, and age.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant with name, height (cm), and age (days).
        """
        self.name = name
        self.height = height
        self.age = age

    def aging(self) -> None:
        """
        Increase the plant's age by one day.
        """
        self.age += 1

    def grow(self) -> None:
        """
        Increase the plant's height by 1 cm.
        """
        self.height += 1

    def get_info(self) -> None:
        """
        Print the plants information in a readable format.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    """
    Simulate one week of growth for multiple plants and display the result.
    """
    time: int = 7
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 80, 40)
    ]
    initial_height: dict[str, int] = {}

    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
        initial_height[plant.name] = plant.height

    for plant in plants:
        day: int = 1
        while day < time:
            plant.grow()
            plant.aging()
            day += 1

    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
        growth = plant.height - initial_height[plant.name]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    ft_plant_growth()
