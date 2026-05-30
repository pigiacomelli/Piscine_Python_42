def water_plants(plant_list: list) -> None:
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print("Error:", error)
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")


def ft_finally_block() -> None:
    print("=== Garden Watering System ===\n")
    plant = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    water_plants(plant)

    print("Testing with error...")
    plant = ["tomato", None]
    water_plants(plant)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    ft_finally_block()
