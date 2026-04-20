from ex0.Card import Card, CardType


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str, damage: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.SPELL
        self.effect_type = effect_type
        self.damage = damage

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["player_mana"]):
            game_state["player_mana"] -= self.cost
            result: dict = {}
            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            return result
        else:
            raise ValueError("Insufficient mana to play spell.")

    def resolve_effect(self, targets: list) -> dict:
        name_targets: list = []
        try:
            for target in targets:
                name_targets.append(target.name)
        except AttributeError:
            raise ValueError(
                "Invalid target: All targets must have a 'name' attribute."
            )

        result = {
            "spell_used": self.name,
            "targets": name_targets,
            "effect": self.effect_type
        }
        return result