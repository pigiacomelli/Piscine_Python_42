def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as error:
        print("Caught ValueError:", error)

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as error:
        print("Caught ZeroDivisionError:", error)

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error)

    print("\nTesting KeyError...")
    try:
        plants = {"rose": "red", "tulip": "yellow"}
        plants["missing_plant"]
    except KeyError as error:
        print("Caught KeyError:", error)

    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
