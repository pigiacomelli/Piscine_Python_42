def input_temperature(temp_str: str) -> int:
    # Convert string to integer (may raise ValueError)
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    # Test with valid input
    try:
        temp = "25"
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    # Test with invalid input
    try:
        temp = "abc"
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()