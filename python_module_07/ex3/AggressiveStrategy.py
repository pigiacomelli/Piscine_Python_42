from ex3.GameStrategy import GameStrategy
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        card_played: list = []
        mana_used: int = 0
        damage_dealt = 0
        actions: dict = {}
        for card in hand[:]:
            if card.cost <= 3:
                card_played.append(card.name)
                if isinstance(card, SpellCard):
                    damage_dealt += card.damage
                elif isinstance(card, CreatureCard):
                    battlefield.append(card)
                mana_used += card.cost
                hand.remove(card)
        for creature in battlefield:
            damage_dealt += creature.attack
        actions = {"cards_played": card_played, "mana_used": mana_used,
                   "targets_attacked": ['Enemy_Player'],
                   "damage_dealt": damage_dealt}
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets):
        weakest: str = available_targets[0].name
        less: int = available_targets[0].health
        if "Enemy_Player" in available_targets:
            return ["Enemy_Player"]
        else:
            for target in available_targets:
                if target.health < less:
                    less = target.health
                    weakest = target.name
        return [weakest]