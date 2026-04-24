import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    # Initial list
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    # ---- List comprehensions ----
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}")

    # ---- Dictionary comprehension (scores) ----
    print()
    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    # ---- Average ----
    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    # ---- High scores ----
    high_scores = {name: score for name, score in scores.items() if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()