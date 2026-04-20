import sys
def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    if not archivist_id or not status:
        sys.stderr.write("[ERROR] Inputs cannot be empty.\n")
        return
    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_id}: {status}\n"
    )

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()