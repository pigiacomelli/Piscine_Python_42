import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        raise ValueError("Unknown operation")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "frost": functools.partial(base_enchantment, 50, "Frost"),
        "arcane": functools.partial(base_enchantment, 50, "Arcane"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _int_handler(arg: int) -> str:
        return f"{arg} damage"

    @dispatcher.register(str)
    def _str_handler(arg: str) -> str:
        return "fireball"

    @dispatcher.register(list)
    def _list_handler(arg: list[Any]) -> str:
        return f"{len(arg)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    disp = spell_dispatcher()
    print(f"Damage spell: {disp(42)}")
    print(f"Enchantment: {disp('heal')}")
    print(f"Multi-cast: {disp([1, 2, 3])}")
    res = disp(3.14)
    if res == "Unknown spell type":
        print(res)


if __name__ == "__main__":
    main()
