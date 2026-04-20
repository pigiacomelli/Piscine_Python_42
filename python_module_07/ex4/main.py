from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 4)
    wizard.rating = 1150

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    rank = 1
    for entry in leaderboard:
        print(f"{rank}. {entry['name']}")
        print(f" Rating: {entry['rating']} ({entry['record']})")
        rank += 1

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(str(report))

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()