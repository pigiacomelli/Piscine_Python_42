from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard


def get_card_rating(card: TournamentCard) -> int:
    return card.calculate_rating()


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}

    def register_card(self, card: TournamentCard) -> str:
        base_id = card.name.lower()
        clean_id = base_id.replace(' ', '_')
        card_id = f"{clean_id}_001"

        self.cards[card_id] = card

        print(f"{card.name} (ID: {card_id}):")
        print(" Interfaces: [Card, Combatable, Rankable]")
        print(f" Rating: {card.rating}")
        print(f" Record: {card.wins}-{card.losses}")

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)

        if c1 is None:
            return {"error": "Card not found"}
        if c2 is None:
            return {"error": "Card not found"}

        if c1.attack_val >= c2.attack_val:
            winner = c1
            loser = c2
            w_id = card1_id
            l_id = card2_id
        else:
            winner = c2
            loser = c1
            w_id = card2_id
            l_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": w_id,
            "loser": l_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        all_cards = list(self.cards.values())
        sorted_cards = sorted(
            all_cards,
            key=get_card_rating,
            reverse=True
        )

        leaderboard = []
        for card in sorted_cards:
            entry = {
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}"
            }
            leaderboard.append(entry)

        return leaderboard

    def generate_tournament_report(self) -> Dict[str, Any]:
        ratings = []
        total_matches = 0

        for card in self.cards.values():
            ratings.append(card.calculate_rating())
            total_matches += card.wins

        avg_rating = 0
        if len(ratings) > 0:
            total_score = sum(ratings)
            count = len(ratings)
            avg_rating = total_score // count

        return {
            "total_cards": len(self.cards),
            "matches_played": total_matches,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }