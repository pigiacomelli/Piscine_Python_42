from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")

            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # ===== Tournament 0 =====
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    battle([
        (flame, normal),
        (heal, defensive),
    ])

    # ===== Tournament 1 =====
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    battle([
        (flame, aggressive),
        (heal, defensive),
    ])

    # ===== Tournament 2 =====
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    battle([
        (aqua, normal),
        (heal, defensive),
        (transform, aggressive),
    ])