import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("No inventory items provided.")
        return

    inventory: dict[str, int] = {}

    # Parsing da linha de comando
    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Invalid format ignored: {arg}")
            continue

        item: str = parts[0]

        try:
            quantity: int = int(parts[1])
        except ValueError:
            print(f"Invalid quantity ignored: {arg}")
            continue

        inventory[item] = quantity

    if len(inventory) == 0:
        print("No valid inventory data.")
        return

    # Estatísticas básicas
    total_items: int = sum(inventory.values())
    unique_items: int = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}\n")

    print("=== Current Inventory ===")

    for item, quantity in inventory.items():
        percentage: float = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")

    # Item mais e menos abundante
    most_abundant: str = max(inventory, key=inventory.get)
    least_abundant: str = min(inventory, key=inventory.get)

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory.get(most_abundant)} units)")
    print(f"Least abundant: {least_abundant} ({inventory.get(least_abundant)} units)")

    # Categorias
    abundant: dict[str, int] = {}
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}

    for item, quantity in inventory.items():
        if quantity >= 5:
            abundant[item] = quantity
        elif quantity >= 3:
            moderate[item] = quantity
        else:
            scarce[item] = quantity

    print("\n=== Item Categories ===")
    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    # Sugestões simples de reposição
    restock: list[str] = [item for item, quantity in inventory.items() if quantity <= 1]

    print("\n=== Management Suggestions ===")
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("Stock levels are healthy.")

    # Demonstração dos métodos do dicionário
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")

    sample_lookup: str = "sword"
    print(f"Sample lookup - '{sample_lookup}' in inventory: {sample_lookup in inventory}")


if __name__ == "__main__":
    main()
