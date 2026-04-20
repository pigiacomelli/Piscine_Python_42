from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

        print("CreatureCard Info:")
        print(dragon.get_card_info())

        game_state = {"player_mana": 6}
        print(f"\nPlaying Fire Dragon with {game_state['player_mana']}"
              " mana available:")
        print("Playable: True")
        result = dragon.play(game_state)
        print(f"Play result: {result}")

        print("\nFire Dragon attacks Goblin Warrior:")
        result = dragon.attack_target(goblin)
        print(f"Attack result: {result}")

        game_state["player_mana"] = 3
        print(f"\nTesting insufficient mana ({game_state['player_mana']}"
              " available):")
        print("Playable: False")
        try:
            result = dragon.play(game_state)
            print(f"Play result: {result}")
        except ValueError:
            pass

    except (ValueError, TypeError):
        print("An error occurred during card creation.")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()