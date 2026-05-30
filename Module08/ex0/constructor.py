import sys
import os
import site


def is_virtual_environment() -> bool:
    return (
        hasattr(sys, "real_prefix") or
        (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_python_path() -> str:
    return sys.executable


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def get_site_packages() -> str:
    try:
        site_packages: list[str] = site.getsitepackages()
        return site_packages[0] if site_packages else "Not found"
    except AttributeError:
        return site.getusersitepackages()


def main() -> None:
    in_venv: bool = is_virtual_environment()

    if not in_venv:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {get_python_path()}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        venv_name: str = get_venv_name()
        venv_path: str = sys.prefix
        site_packages: str = get_site_packages()

        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {get_python_path()}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
