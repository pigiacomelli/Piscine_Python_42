import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        print("---")
        print()
        content = []
        for line in file:
            print(line, end="")
            content.append(line)
        print()
        print("---")
        file.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    print()
    # Transform data
    print("Transform data:")
    print("---")
    print()

    transformed = []
    for line in content:
        new_line = line.rstrip("\n") + "#\n"
        print(new_line, end="")
        transformed.append(new_line)
    print()
    print("---")

    # Ask user for filename
    new_filename = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        new_file = open(new_filename, "w")
        for line in transformed:
            new_file.write(line)
        new_file.close()
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(f"Error writing file '{new_filename}': {e}")


if __name__ == "__main__":
    main()