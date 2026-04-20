def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2500
    }

    achievements: dict[str, set[str]] = {
        "alice": {"first_kill", "level_10", "boss_slayer"},
        "bob": {"first_kill"},
        "charlie": {"level_10", "boss_slayer", "collector"},
        "diana": {"first_kill", "collector"}
    }

    print("=== List Comprehension Examples ===")

    high_scorers = [name for name, score in players.items() if score > 2000]
    doubled_scores = [score * 2 for score in players.values()]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}\n")

    print("=== Dict Comprehension Examples ===")

    high_score_map = {
        name: score
        for name, score in players.items()
        if score > 2000
    }

    achievement_counts = {
        name: len(achievements[name])
        for name in achievements
    }

    print(f"Player scores (filtered): {high_score_map}")
    print(f"Achievement counts: {achievement_counts}\n")

    print("=== Set Comprehension Examples ===")

    unique_achievements = {
        achievement
        for player_set in achievements.values()
        for achievement in player_set
    }

    unique_players = {name for name in players}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}\n")

    print("=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(players.values()) / total_players
    top_player = max(players, key=players.get)

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({players[top_player]} points)")


if __name__ == "__main__":
    main()
