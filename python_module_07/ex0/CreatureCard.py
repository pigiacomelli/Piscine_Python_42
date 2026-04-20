from ex0.Card import Card, CardType


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.CREATURE
        self.attack = attack
        self.health = health
        if attack < 0 or health < 0:
            raise ValueError

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["player_mana"]):
            game_state["player_mana"] -= self.cost
            result: dict = {}
            result = {"card_played": self.name, "mana_used": self.cost,
                      "effect": "Creature summoned to battlefield"}
            return result
        else:
            raise ValueError

    def get_card_info(self) -> dict:
        info: dict = {}
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type.value, "attack": self.attack,
                "health": self.health}
        return info

    def attack_target(self, target) -> dict:
        try:
            name: str = target.name
        except AttributeError:
            raise ValueError
        combat_resolved: bool
        if self.attack >= target.health:
            combat_resolved = True
            target.health = 0
        else:
            target.health -= self.attack
            combat_resolved = False
        result = {"attacker": self.name, "target": name, "damage_dealt":
                  self.attack, "combat_resolved": combat_resolved}
        return result