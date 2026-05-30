import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        arc_id: str = input("Input Stream active. Enter archivist ID: ")
        status: str = input("Input Stream active. Enter status report: ")
    except (KeyboardInterrupt, EOFError):
        sys.stderr.write("\n[ALERT] Communication interrupted by user.\n")
        sys.exit(1)

    sys.stdout.write(
        f"[STANDARD] Archive status from {arc_id}: {status}\n"
        )
    sys.stderr.write(
        "\n[ALERT] System diagnostic: Communication channels verified"
        )
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
