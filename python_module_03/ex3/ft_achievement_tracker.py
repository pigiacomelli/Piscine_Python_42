def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }

    bob: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_achievements: set[str] = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_to_all: set[str] = alice & bob & charlie
    print(f"Common to all players: {common_to_all}")


    rare_achievements: set[str] = set()

    for achievement in all_achievements:
        count: int = 0

        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1

        if count == 1:
            rare_achievements.add(achievement)

    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_bob_common: set[str] = alice & bob
    alice_unique: set[str] = alice - bob
    bob_unique: set[str] = bob - alice

    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
