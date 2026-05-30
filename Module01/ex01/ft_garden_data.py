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

    def display(self) -> None:
        """
        Print the plant's information in a readable format.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """
    Create a list of plant's and display their information.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    ft_garden_data()
