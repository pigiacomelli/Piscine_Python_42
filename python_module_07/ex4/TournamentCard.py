from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_val: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "effect": "Entered tournament arena"
        }

    def is_playable(self, available_mana: int) -> bool:
        if self.cost <= available_mana:
            return True
        else:
            return False

    def get_card_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": "TournamentCard",
            "rating": self.rating
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_val,
            "combat_type": "tournament_melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        self.health -= incoming_damage
        is_alive = False
        if self.health > 0:
            is_alive = True

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": is_alive
        }

    def get_combat_stats(self) -> Dict[str, int]:
        return {"attack": self.attack_val, "health": self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        points = 16 * wins
        self.rating += points

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        points = 16 * losses
        self.rating -= points

    def get_rank_info(self) -> Dict[str, Any]:
        record_string = f"{self.wins}-{self.losses}"
        return {
            "rating": self.rating,
            "record": record_string
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        stats = self.get_rank_info()
        combat_stats = self.get_combat_stats()
        stats.update(combat_stats)
        return stats