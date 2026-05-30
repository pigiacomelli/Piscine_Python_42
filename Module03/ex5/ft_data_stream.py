import random
import typing

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        event: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while event:
        index = random.randint(0, len(event) - 1)
        yield event.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream: typing.Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(stream))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
