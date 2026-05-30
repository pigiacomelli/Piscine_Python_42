from collections.abc import Callable
from typing import Any


def spell_combiner(
    spell1: Callable[..., Any], spell2: Callable[..., Any]
) -> Callable[..., tuple[Any, Any]]:
    return lambda *a, **k: (spell1(*a, **k), spell2(*a, **k))


def power_amplifier(
    base_spell: Callable[..., Any], multiplier: int
) -> Callable[..., Any]:
    def amplified(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[..., bool], spell: Callable[..., Any]
) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return wrapper


def spell_sequence(
    spells: list[Callable[..., Any]]
) -> Callable[..., list[Any]]:
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def main() -> None:
    print("Testing spell combiner...")
    comb = spell_combiner(fireball, heal)
    res = comb("Dragon", 50)
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("Testing power amplifier...")
    amp = power_amplifier(fireball, 3)
    amp("Goblin", 10)
    print("Original: 10, Amplified: 30")


if __name__ == "__main__":
    main()
