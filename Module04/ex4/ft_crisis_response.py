def handle_crisis(filename, mode) -> None:
    if mode:
        print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: An unexpected error happened: {e}")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_crisis("lost_archive.txt", False)
    handle_crisis("classified_vault.txt", False)
    handle_crisis("standard_archive.txt", True)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
