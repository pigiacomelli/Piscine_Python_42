from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def run_tournament(
    name: str,
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"{name}")
    
    # Extrair os nomes pra compor o header bonitinho como no exemplo
    opp_names = []
    for factory, strategy in opponents:
        fact_name = factory.__class__.__name__.replace("Factory", "")
        fact_name = fact_name.replace("Creature", "")
        strat_name = strategy.__class__.__name__.replace("Strategy", "")
        opp_names.append(f"({fact_name}+{strat_name})")
    print(f"[ {', '.join(opp_names)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    
    # Criar instâncias das criaturas para o torneio
    creatures = [(f.create_base(), s) for f, s in opponents]

    # Round Robin (cada um luta contra os demais que vêm a seguir)
    try:
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                c1, s1 = creatures[i]
                c2, s2 = creatures[j]
                
                print("* Battle *")
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")
                
                # Turno 1
                for action in s1.act(c1):
                    print(action)
                # Turno 2
                for action in s2.act(c2):
                    print(action)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    norm_s = NormalStrategy()
    def_s = DefensiveStrategy()
    agg_s = AggressiveStrategy()

    run_tournament(
        "Tournament 0 (basic)",
        [(flame_f, norm_s), (heal_f, def_s)]
    )
    
    print("")
    run_tournament(
        "Tournament 1 (error)",
        [(flame_f, agg_s), (heal_f, def_s)]
    )

    print("")
    run_tournament(
        "Tournament 2 (multiple)",
        [(aqua_f, norm_s), (heal_f, def_s), (trans_f, agg_s)]
    )
    