class Plant:
    """
    Base plant class with protected height and basic growth behavior.
    """
    type: str = "Plant"

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize plant with name and initial height.
        """
        self.name: str = name
        self.__height: int = 0
        self.age: int = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int) -> None:
        """
        Set plant height, rejecting negative values.
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height

    def set_age(self, new_age: int) -> None:
        """
        Set plant age, rejecting negative values.
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} "
                  "days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.age = new_age

    def get_height(self) -> int:
        """
        Return current plant height.
        """
        return self.__height

    def grow(self) -> None:
        """
        Increase plant height by 1 cm.
        """
        self.set_height(self.__height + 1)
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """
        Return basic plant information.
        """
        return f"{self.name}: {self.get_height()}cm, {self.age} days"


class FloweringPlant(Plant):
    """
    Plant that produces flowers and can bloom.
    """
    type: str = "FloweringPlant"

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize flowering plant with color.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """
        Return blooming status.
        """
        return "(blooming)"

    def get_info(self) -> str:
        """
        Return flowering plant information.
        """
        return (
            f"{self.name}: {self.get_height()}cm, {self.age} days, "
            f"{self.color} flowers {self.bloom()}"
        )


class PrizeFlower(FloweringPlant):
    """
    Special flowering plant that gives bonus points.
    """
    type: str = "PrizeFlower"

    def __init__(
            self, name: str, height: int, age: int, color: str, points: int
            ) -> None:
        """
        Initialize prize flower with bonus points.
        """
        super().__init__(name, height, age, color)
        self.points: int = points

    def get_info(self) -> str:
        """
        Return prize flower information including points.
        """
        base: str = super().get_info()
        return f"{base}, Prize points: {self.points}\n"


class Garden:
    """
    Represents a garden containing multiple plants and growth statistics.
    """
    def __init__(self, owner: str, plants_list: list[Plant]) -> None:
        """
        Initialize garden and classify plant types.
        """
        self.owner: str = owner
        self.plants_list: list[Plant] = plants_list

        self.regular: int = 0
        self.flowering: int = 0
        self.prize_flower: int = 0
        self.growth: int = 0

        for plant in self.plants_list:
            print(f"Added {plant.name} to {self.owner}'s garden")
            if plant.type == "PrizeFlower":
                self.prize_flower += 1
            elif plant.type == "FloweringPlant":
                self.flowering += 1
            else:
                self.regular += 1

    def size(self) -> int:
        """
        Return number of plants in the garden.
        """
        total: int = 0
        for _ in self.plants_list:
            total += 1
        return total

    def help_all_grow(self, times: int = 1) -> None:
        """
        Make all plants grow a given number of times.
        """
        print(f"{self.owner} is helping all plants grow...")
        for _ in range(times):
            for plant in self.plants_list:
                plant.grow()
                self.growth += 1

    def get_info(self) -> None:
        """
        Print a full garden report.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants_list:
            print(f"- {plant.get_info()}")

        print(f"Plants added: {self.size()}, Total growth: {self.growth}cm")
        print(
            f"Plant types: {self.regular} regular, "
            f"{self.flowering} flowering, "
            f"{self.prize_flower} prize flowers"
        )


class GardenManager:
    """
    Manages multiple gardens and calculates scores.
    """
    class GardenStats:
        """
        Provides statistical calculations for gardens.
        """
        @staticmethod
        def score(garden: Garden) -> int:
            """
            Calculate score based on plant height and prize points.
            """
            points: int = 0
            for plant in garden.plants_list:
                points += plant.get_height()
                if isinstance(plant, PrizeFlower):
                    points += plant.points
            return points

    def __init__(self, gardens_list: list[Garden]) -> None:
        """
        Initialize manager with a list of gardens.
        """
        self.gardens: list[Garden] = gardens_list
        self.stats = self.GardenStats()

    @classmethod
    def create_garden_network(cls,
                              gardens_list: list[Garden]) -> "GardenManager":
        """
        Factory method to create a GardenManager.
        """
        return cls(gardens_list)

    def number_of_gardens(self) -> int:
        """
        Return number of managed gardens.
        """
        total: int = 0
        for _ in self.gardens:
            total += 1
        return total

    @staticmethod
    def height_validation(height: int) -> bool:
        """
        Validate height value.
        """
        return isinstance(height, int) and height >= 0

    def get_info(self) -> None:
        """
        Print manager summary and garden scores.
        """
        print("Garden scores: - ", end="")
        first = True
        for garden in self.gardens:
            if not first:
                print(", ", end="")
            print(f"{garden.owner}: {self.stats.score(garden)} points", end="")
            first = False
        print(f"\nTotal gardens managed: {self.number_of_gardens()}")


def ft_garden_analytics() -> None:
    """
    Run the garden management system demo.
    """
    print("=== Garden Management System Demo ===\n")

    alice_plants: list[Plant] = [
        Plant("Oak Tree", 100, 500),
        FloweringPlant("Rose", 25, 30, "red"),
        PrizeFlower("Sunflower", 50, 90, "yellow", 10),
    ]

    alfredo_plants: list[Plant] = [
        Plant("Pine", 80, 10),
        FloweringPlant("Tulips", 15, 5, "blue"),
        PrizeFlower("Orchid", 36, 20, "white", 25),
    ]

    alice_garden = Garden("Alice", alice_plants)
    print()
    alfredo_garden = Garden("Alfredo", alfredo_plants)

    print()
    alice_garden.help_all_grow(1)
    print()
    alfredo_garden.help_all_grow(1)

    print()
    alice_garden.get_info()

    print()
    alfredo_garden.get_info()
    print()

    manager = GardenManager.create_garden_network([alice_garden,
                                                   alfredo_garden])
    manager.get_info()


if __name__ == "__main__":
    ft_garden_analytics()
