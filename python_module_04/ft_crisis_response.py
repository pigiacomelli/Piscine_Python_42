def helper(filename: str) -> None:
    try:
        with open(filename, "r") as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered '{data}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    helper("lost_archive.txt")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    helper("classified_vault.txt")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    helper("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
