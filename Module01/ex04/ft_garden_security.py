class SecurePlant:
    """
    Plant with protected height and age, rejecting invalid values.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize plant with name, height (cm) and age (days).
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int) -> None:
        """
        Update height, rejecting negative values.
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def get_height(self) -> int:
        """
        Return current height.
        """
        return self.__height

    def set_age(self, new_age: int) -> None:
        """
        Update age, rejecting negative values.
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days "
                  "[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_age(self) -> int:
        """
        Return current age.
        """
        return self.__age

    def get_info(self) -> None:
        """
        Print plant name, height and age.
        """
        print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")

    def grow(self) -> None:
        """
        Increase height by 1 cm.
        """
        self.set_height(self.__height + 1)

    def age(self) -> None:
        """
        Increase age by 1 day.
        """
        self.set_age(self.__age + 1)


def ft_garden_security() -> None:
    """
    Demonstrate validation and security checks.
    """
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print()
    plant.set_height(-5)
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
