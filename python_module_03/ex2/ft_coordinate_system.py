import math


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    parts = coord_str.split(",")

    if len(parts) != 3:
        raise ValueError("Invalid coordinate format")

    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])

    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)
    position: tuple[int, int, int] = (10, 20, 5)

    print(f"Position created: {position}")

    distance = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")

    coord_input = "3,4,0"
    print(f'Parsing coordinates: "{coord_input}"')

    try:
        parsed_position = parse_coordinates(coord_input)
        print(f"Parsed position: {parsed_position}")

        distance = calculate_distance(origin, parsed_position)
        print(f"Distance between {origin} and {parsed_position}: {distance}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")

    print()

    
    invalid_input = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_input}"')

    try:
        parse_coordinates(invalid_input)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, Args: {error.args}")

    print("\nUnpacking demonstration:")

    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
