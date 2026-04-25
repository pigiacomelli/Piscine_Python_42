# construct.py

import sys
import os
import site


def in_virtualenv() -> bool:
    # Works for venv and virtualenv
    return (
        hasattr(sys, "real_prefix") or
        (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_venv_name(path: str) -> str:
    return os.path.basename(path)


def main():
    print()

    if in_virtualenv():
        # ===== INSIDE VENV =====
        print("MATRIX STATUS: Welcome to the construct")

        python_path = sys.executable
        venv_path = sys.prefix
        venv_name = get_venv_name(venv_path)

        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        # site-packages location
        try:
            paths = site.getsitepackages()
            if paths:
                print("\nPackage installation path:")
                print(paths[0])
        except Exception:
            pass

    else:
        # ===== OUTSIDE VENV =====
        print("MATRIX STATUS: You're still plugged in")

        python_path = sys.executable

        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()