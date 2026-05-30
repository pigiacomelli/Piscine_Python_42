FILENAME = "new_discovery.txt"


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {FILENAME}")

    file = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    content = "[ENTRY 001] New quantum algorithm discovered\n\
[ENTRY 002] Efficiency increased by 347%\n\
[ENTRY 003] Archived by Data Archivist trainee\n"

    file.write(content)
    print(content)
    print("Data inscription complete. Storage unit sealed.")
    file.close()
    print(f"Archive '{FILENAME}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
