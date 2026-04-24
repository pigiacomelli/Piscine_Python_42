import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    # ---- Parse arguments ----
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty = arg.split(":", 1)

        # Check duplicate
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        # Convert quantity
        try:
            quantity = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity

    # ---- Display inventory ----
    print(f"Got inventory: {inventory}")

    # ---- Item list ----
    items = list(inventory.keys())
    print(f"Item list: {items}")

    # ---- Total quantity ----
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    # ---- Percentages ----
    for item in items:
        percentage = (inventory[item] / total) * 100 if total > 0 else 0
        print(f"Item {item} represents {round(percentage, 1)}%")

    # ---- Most / least abundant ----
    most_item = None
    least_item = None

    for item in items:
        if most_item is None or inventory[item] > inventory[most_item]:
            most_item = item
        if least_item is None or inventory[item] < inventory[least_item]:
            least_item = item

    if most_item:
        print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
    if least_item:
        print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

    # ---- Add new item ----
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()