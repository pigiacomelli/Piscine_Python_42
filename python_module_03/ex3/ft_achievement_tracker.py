import random


def gen_player_achievements() -> set:
    achievements_pool = [
        "First Steps", "Survivor", "Speed Runner", "Treasure Hunter",
        "Master Explorer", "Crafting Genius", "Strategist",
        "Collector Supreme", "Untouchable", "Unstoppable",
        "Sharp Mind", "Boss Slayer", "World Savior",
        "Hidden Path Finder"
    ]

    # Random number of achievements
    count = random.randint(1, len(achievements_pool))

    # Random selection without duplicates
    return set(random.sample(achievements_pool, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    # Display players
    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    # ---- All distinct achievements ----
    all_achievements = set()
    for ach in players.values():
        all_achievements = all_achievements.union(ach)

    print(f"All distinct achievements: {all_achievements}")
    print()
    # ---- Common achievements ----
    common_achievements = None
    for ach in players.values():
        if common_achievements is None:
            common_achievements = ach
        else:
            common_achievements = common_achievements.intersection(ach)

    print(f"Common achievements: {common_achievements}")

    # ---- Unique achievements per player ----
    for name, ach in players.items():
        others = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)

        unique = ach.difference(others)
        print(f"Only {name} has: {unique}")
    print()
    # ---- Missing achievements per player ----
    for name, ach in players.items():
        missing = all_achievements.difference(ach)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()