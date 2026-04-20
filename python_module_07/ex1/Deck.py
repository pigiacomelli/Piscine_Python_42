import random
from typing import List
from ex0.Card import Card, CardType


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            raise IndexError
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: int = 0
        total_cards: int = len(self.cards)

        for card in self.cards:
            total_cost += card.cost
            if card.type == CardType.CREATURE:
                creatures += 1
            elif card.type == CardType.SPELL:
                spells += 1
            elif card.type == CardType.ARTIFACT:
                artifacts += 1

        avg_cost: float = 0.0
        if total_cards > 0:
            avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }