class Plant:
    """
    Represents a plant with a name, height, and age.
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
        Print the plant's information in a readable format.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    """
    Create multiple plants from initial data and display them.
    """
    plants_info: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = [Plant(name, height, age) for name, height, age in plants_info]
    count: int = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        count += 1
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    ft_plant_factory()
