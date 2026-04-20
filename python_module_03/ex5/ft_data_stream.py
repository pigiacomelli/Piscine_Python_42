from typing import Generator


# Generator simples de eventos
def game_event_stream(limit: int) -> Generator[str, None, None]:
    for i in range(1, limit + 1):
        if i % 3 == 0:
            yield f"Event {i}: Player leveled up"
        elif i % 5 == 0:
            yield f"Event {i}: Player found treasure"
        else:
            yield f"Event {i}: Player attacked monster"


# Generator Fibonacci
def fibonacci(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


# Generator de números primos
def prime_numbers(n: int) -> Generator[int, None, None]:
    count: int = 0
    number: int = 2

    while count < n:
        is_prime: bool = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            yield number
            count += 1

        number += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    total_events: int = 0
    level_up_events: int = 0
    treasure_events: int = 0

    print("Processing 20 game events...\n")

    for event in game_event_stream(20):
        print(event)
        total_events += 1

        if "leveled up" in event:
            level_up_events += 1
        if "treasure" in event:
            treasure_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"Level-up events: {level_up_events}")
    print(f"Treasure events: {treasure_events}")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    for number in fibonacci(10):
        print(number, end=" ")

    print("\nPrime numbers (first 5): ", end="")
    for prime in prime_numbers(5):
        print(prime, end=" ")

    print()


if __name__ == "__main__":
    main()
