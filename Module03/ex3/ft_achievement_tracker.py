import random

ACHIEVEMENTS: list[str] = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind',
        'Hidden Path Finder'
    ]

PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    qnty: int = random.randint(3, 8)
    return set(random.sample(ACHIEVEMENTS, qnty))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    player_sets: dict[str, set[str]] = {}
    for player in PLAYERS:
        player_sets[player] = gen_player_achievements()
        print(f"Player {player}: {player_sets[player]}")

    distinct: set[str] = set()
    for achievements in player_sets.values():
        distinct = distinct.union(achievements)
    print(f"\nAll distinct achievements: {distinct}")

    common: set[str] = player_sets[PLAYERS[0]].copy()
    for player in PLAYERS[1:]:
        common = common.intersection(player_sets[player])
    print(f"\nCommon achievements: {common}\n")

    for player in PLAYERS:
        others_unions: set[str] = set()

        for other in PLAYERS:
            if other != player:
                others_unions = others_unions.union(player_sets[other])

        unique = player_sets[player].difference(others_unions)
        print(f"Only {player} has: {unique}")

    print()

    for player in PLAYERS:
        missing: set[str] = set(ACHIEVEMENTS).difference(player_sets[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
