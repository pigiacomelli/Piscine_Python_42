from ex0.Card import Card, CardType


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.ARTIFACT
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["player_mana"]):
            game_state["player_mana"] -= self.cost
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
            return result
        else:
            raise ValueError("Insufficient mana to play artifact.")

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            result = {
                "artifact": self.name,
                "durability_remaining": self.durability,
                "effect_activated": self.effect
            }
            return result
        else:
            raise ValueError("Artifact is broken (0 durability).")