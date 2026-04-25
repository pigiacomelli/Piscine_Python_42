from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2):
    print("Testing battle")

    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    test_factory(aqua)

    battle(flame, aqua)