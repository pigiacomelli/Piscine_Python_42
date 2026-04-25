class Plant:
    class _Stats:
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0

        def display(self):
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant._Stats()

    def grow(self):
        self.height = round(self.height + 8.0, 1)
        self._stats.grow += 1

    def age_one_day(self):
        self.age += 20
        self._stats.age += 1

    def show(self):
        self._stats.show += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self):
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_shade(self):
        print(f"{self._shade_calls} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0
    def grow(self):
        self.height = round(self.height + 30.0, 1)
        self._stats.grow += 1
    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def show_stats(plant: Plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if isinstance(plant, Tree):
        plant.show_shade()


def ft_garden_analytics():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_one_day()
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_stats(unknown)

if __name__ == "__main__":
    ft_garden_analytics()