FILENAME = "ancient_fragment.txt"


def main() -> None:

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {FILENAME}")

    try:
        file = open(FILENAME, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(file.read())
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
