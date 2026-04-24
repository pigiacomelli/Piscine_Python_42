import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx = random.randrange(len(events))
        event = events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    # ---- Generate 1000 events ----
    generator = gen_event()

    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    # ---- Build list of 10 events ----
    events_list = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    # ---- Consume events ----
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()