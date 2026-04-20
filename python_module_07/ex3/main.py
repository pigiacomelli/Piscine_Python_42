from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print(f"Supported types: {factory.get_supported_types()}")

    engine.start_game(deck_size=10)

    print("\nSimulating aggressive turn...")
    hand_display = [f"{card.name} ({card.cost})" for card in engine.hand]
    print(f"Hand: {hand_display}")

    print("\nTurn execution:")
    actions = engine.play_turn()

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {actions}")

    print("\nGame Report:")
    report = {
        'turns_simulated': 1,
        'strategy_used': strategy.get_strategy_name(),
        'total_damage': actions['damage_dealt'],
        'cards_played_count': len(actions['cards_played'])
    }
    print(str(report))

    print("\nAbstract Factory + Strategy Pattern: Maximum "
          "flexibility achieved!")


if __name__ == "__main__":
    main()