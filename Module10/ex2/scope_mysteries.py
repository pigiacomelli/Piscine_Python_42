from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def accumulate(power: int) -> int:
        nonlocal total
        total += power
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    ca = mage_counter()
    cb = mage_counter()
    print(f"counter_a call 1: {ca()}")
    print(f"counter_a call 2: {ca()}")
    print(f"counter_b call 1: {cb()}")

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("Testing enchantment factory...")
    f1 = enchantment_factory("Flaming")
    f2 = enchantment_factory("Frozen")
    print(f1("Sword"))
    print(f2("Shield"))

    print("Testing memory vault...")
    mv = memory_vault()
    mv["store"]("secret", 42)
    print(f"Recall 'secret': {mv['recall']('secret')}")
    print(f"Recall 'unknown': {mv['recall']('unknown')}")


if __name__ == "__main__":
    main()
