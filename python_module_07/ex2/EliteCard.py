from typing import Any, Dict, List
from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_points: int,
                 health_points: int, defense_points: int,
                 effect_type: str, combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.ELITE
        self.attack_points = attack_points
        self.health_points = health_points
        self.defense_points = defense_points
        self.combat_type = combat_type
        self.effect_type = effect_type
        self.mana = 0

        if attack_points < 0 or health_points < 0:
            raise ValueError("Attack and Health must be non-negative.")

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        if not self.is_playable(game_state["player_mana"]):
            raise ValueError("Insufficient mana to play elite card.")

        game_state["player_mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        try:
            target_name = target.name
        except AttributeError:
            target_name = "Target"

        raw_damage = self.attack_points
        target.defend(raw_damage)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": raw_damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_blocked = self.defense_points
        damage_taken = incoming_damage - damage_blocked

        if damage_taken < 0:
            damage_taken = 0

        self.health_points -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health_points > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.attack_points,
            "health": self.health_points,
            "defense": self.defense_points,
            "type": self.combat_type
        }

    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        target_names = []
        for t in targets:
            try:
                target_names.append(t.name)
            except AttributeError:
                target_names.append(str(t))
        mana_cost = len(targets) * 2

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": target_names,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            "effect_type": self.effect_type,
            "spell_power": self.cost * 2
        }