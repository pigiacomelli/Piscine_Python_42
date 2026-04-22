def input_temperature(temp_str: str) -> int:
    # Convert to integer (may raise ValueError)
    temp = int(temp_str)

    # Validate range for plants
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_values = ["25", "abc", "100", "-50"]

    for temp in test_values:
        try:
            print(f"Input data is '{temp}'")
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()