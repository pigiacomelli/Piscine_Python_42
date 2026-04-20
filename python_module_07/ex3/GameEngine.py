from typing import List, Dict, Any
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck: List[Card] = []
        self.hand: List[Card] = []
        self.battlefield: List[Card] = []

    def start_game(self, deck_size: int = 10) -> None:
        deck_data = self.factory.create_themed_deck(deck_size)
        self.deck = deck_data["deck"]
        self.hand = []
        self.battlefield = []
        for _ in range(3):
            if self.deck:
                self.hand.append(self.deck.pop(0))

    def play_turn(self) -> Dict[str, Any]:
        if self.deck:
            self.hand.append(self.deck.pop(0))
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        return result