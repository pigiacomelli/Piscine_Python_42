class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    plant.show()
    print()

    plant.set_height(25)
    plant.set_age(30)
    print()

    plant.set_height(-5)
    plant.set_age(-10)

    print()
    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()