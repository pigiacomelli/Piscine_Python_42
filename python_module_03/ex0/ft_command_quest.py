import sys


def main() -> None:
    argus = sys.argv
    total_args = len(argus)

    print("=== Command Quest ===")

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {argus[0]}")
    else:
        i: int = 1
        print(f"Program name: {argus[0]}")
        print(f"Arguments received: {total_args - 1}")

        while i < total_args:
            print(f"Argument {i}: {argus[i]}")
            i += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
