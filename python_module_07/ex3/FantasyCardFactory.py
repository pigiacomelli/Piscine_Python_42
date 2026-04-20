import random
from typing import Dict, List, Any
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: Any) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power == "dragon":
                return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            else:
                return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        elif isinstance(name_or_power, int):
            if name_or_power > 4:
                return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            else:
                return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        else:
            return CreatureCard("whisper", 1, "Common", 1, 1)

    def create_spell(self, name_or_power: Any) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power == "fireball":
                return SpellCard("Fireball", 6, "Epic",
                                 "Deal 8 damage to target", 8)
            else:
                return SpellCard("Lightning Bolt", 3, "Common",
                                 "Deal 3 damage to target", 3)
        elif isinstance(name_or_power, int):
            if name_or_power >= 6:
                return SpellCard("Fireball", 6, "Epic",
                                 "Deal 8 damage to target", 8)
            else:
                return SpellCard("Lightning Bolt", 3, "Common",
                                 "Deal 3 damage to target", 3)
        else:
            return SpellCard("Night Fire", 1, "Common",
                             "Deal 1 damage to target", 1)

    def create_artifact(self, name_or_power: Any) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power == "excalibur":
                return ArtifactCard("Excalibur", 10, "Legendary",
                                    "Boosts attack by 10", 10)
            else:
                return ArtifactCard("Wooden Shield", 2, "Common",
                                    "Blocks 2 damage", 5)
        elif isinstance(name_or_power, int):
            if name_or_power >= 5:
                return ArtifactCard("Excalibur", 10, "Legendary",
                                    "Boosts attack by 10", 10)
            else:
                return ArtifactCard("Wooden Shield", 2, "Common",
                                    "Blocks 2 damage", 5)
        else:
            return ArtifactCard("Broken Sword", 1, "Common",
                                "Useless", 1)

    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        deck: List[Card] = []
        for _ in range(size):
            card_type: str = random.choice(["creature", "spell", "artifact"])
            power: int = random.randint(1, 10)

            if card_type == "creature":
                deck.append(self.create_creature(power))
            elif card_type == "spell":
                deck.append(self.create_spell(power))
            else:
                deck.append(self.create_artifact(power))

        return {"deck": deck}

    def get_supported_types(self) -> List[str]:
        return ["creature", "spell", "artifact"]