import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")

        # Split input
        parts = user_input.split(",")

        # Check correct number of values
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []
        valid = True

        for p in parts:
            p = p.strip()
            try:
                value = float(p)
                coords.append(value)
            except ValueError as e:
                print(f"Error on parameter '{p}': {e}")
                valid = False
                break

        if valid:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    # First coordinates
    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    # Distance to center (0,0,0)
    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    # Second coordinates
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    # Distance between two points
    dist_points = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between points: {round(dist_points, 4)}")


if __name__ == "__main__":
    main()