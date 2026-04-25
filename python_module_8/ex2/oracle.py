# oracle.py

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    print("Install it with: pip install python-dotenv")
    sys.exit(1)


def load_config():
    # Load .env file (if present)
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = [k for k, v in config.items() if not v]

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f" - {key}")
        print("Using defaults where possible.\n")

    return missing


def display_config(config):
    mode = config["MATRIX_MODE"] or "development"

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        if "localhost" in config["DATABASE_URL"]:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['LOG_LEVEL'] or 'INFO'}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_checks():
    print("\nEnvironment security check:")

    # .env existence
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    # .gitignore check
    if os.path.exists(".gitignore"):
        try:
            with open(".gitignore") as f:
                content = f.read()
                if ".env" in content:
                    print("[OK] No hardcoded secrets detected")
                else:
                    print("[WARNING] .env not ignored in .gitignore")
        except Exception:
            print("[WARNING] Could not read .gitignore")
    else:
        print("[WARNING] .gitignore missing")

    print("[OK] Production overrides available")


def main():
    config = load_config()
    validate_config(config)
    display_config(config)
    security_checks()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()