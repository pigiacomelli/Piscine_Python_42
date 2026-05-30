import math
CENTER_COORDS: tuple[float, float, float] = (0.0, 0.0, 0.0)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        entry: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts: list[str] = entry.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords: list[float] = []

        for part in parts:
            text = part.strip()
            try:
                coords.append(float(text))
            except ValueError as e:
                print(f"Error on parameter '{text}': {e}")
                break
        else:
            return (coords[0], coords[1], coords[2])


def calculate_distance(
        pos1: tuple[float, float, float],
        pos2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")

    pos1 = get_player_pos()
    x, y, z = pos1

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")

    print(
        f"Distance to center: "
        f"{round(calculate_distance(pos1, CENTER_COORDS), 4)}\n"
        )

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(calculate_distance(pos1, pos2), 4)}"
        )


if __name__ == "__main__":
    main()
