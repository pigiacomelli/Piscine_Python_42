from ex1.capabilities import HealCapability, TransformCapability
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory


def test_healing_capability() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    print("base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    if isinstance(base_creature, HealCapability):
        print(base_creature.heal())
    print("evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, HealCapability):
        print(evolved_creature.heal())


def test_transform_capability() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    print("base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    if isinstance(base_creature, TransformCapability):
        print(base_creature.transform())
        print(base_creature.attack())
        print(base_creature.revert())
    print("evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.transform())
        print(evolved_creature.attack())
        print(evolved_creature.revert())


if __name__ == "__main__":
    test_healing_capability()
    print()
    test_transform_capability()
