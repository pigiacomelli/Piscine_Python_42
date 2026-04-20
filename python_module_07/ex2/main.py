from ex2.EliteCard import EliteCard


class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.health_points = 10
        self.defense_points = 0

    def defend(self, damage):
        self.health_points -= damage


def main():
    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")

    warrior = EliteCard("Arcane Warrior", 5, "Legendary", 5, 20, 3, "Fire",
                        "melee")
    warrior.mana = 4

    print("\nCombat phase:")
    enemy = Enemy()
    print(f"Attack result: {warrior.attack(enemy)}")

    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print("Spell cast: "
          f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()