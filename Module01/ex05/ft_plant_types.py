class Plant:
    """
    Base class for all plant types.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize plant with name, height (cm) and age (days).
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flowering plant.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize flower with color attribute.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Display blooming message.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """
        Print flower details and trigger bloom.
        """
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )
        self.bloom()


class Tree(Plant):
    """
    Represents a tree with trunk diameter and shade calculation.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """
        Initialize tree with trunk diameter.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        calculate and display shade area.
        """
        shade: int = round(self.trunk_diameter * 1.5)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        """
        Print tree details and shade information.
        """
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    """
    Represents a vegetable with harvest season and nutrition data.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """
        Initialize vegetable with harvest season and nutrition.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        """
        Display nutritional information.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> None:
        """
        Print vegetable details and nutrition.
        """
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )
        self.nutritional()


def ft_plant_types() -> None:
    """
    Demonstrate different plant types and their behaviors.
    """
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    cactus = Flower("Cactus", 120, 90, "green")

    oak = Tree("Oak", 500, 1825, 50)
    spruce = Tree("Spruce", 850, 2000, 60)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    corn = Vegetable("Corn", 150, 100, "summer", "vitamin B")

    rose.get_info()
    cactus.get_info()
    print()
    oak.get_info()
    spruce.get_info()
    print()
    tomato.get_info()
    corn.get_info()


if __name__ == "__main__":
    ft_plant_types()
