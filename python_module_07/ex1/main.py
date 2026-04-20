from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types..")

    deck = Deck()

    dragon = CreatureCard("Fire Dragon", 7, "Legendary", 7, 5)
    crystal = ArtifactCard("Mana Crystal", 2, "Common", 10,
                           "Permanent: +1 mana per turn")
    bolt = SpellCard("Lightning Bolt", 3, "Common",
                     "Deal 3 damage to target", 3)

    deck.add_card(dragon)
    deck.add_card(crystal)
    deck.add_card(bolt)

    print(f"Deck stats: {deck.get_deck_stats()}\n")
    print("Drawing and playing cards:")
    game_state = {"player_mana": 20}

    try:
        for _ in range(3):
            card = deck.draw_card()
            print(f"\nDrew: {card.name} ({card.type.value})")

            result = card.play(game_state)
            print(f"Play result: {result}")
    except IndexError:
        print("Deck is empty!")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()