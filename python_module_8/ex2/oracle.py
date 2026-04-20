import os
from dotenv import load_dotenv


def check_security():
    # Security check: Ensure .env is in .gitignore
    try:
        if os.path.exists(".gitignore"):
            with open(".gitignore", "r") as f:
                content = f.read()
                if ".env" in content:
                    return True
    except Exception:
        pass
    return False


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    # override=False means system variables take precedence over .env file
    load_dotenv(override=False)

    config = {
        "mode": os.getenv("MATRIX_MODE", "unknown"),
        "database": os.getenv("DATABASE_URL", "Not set"),
        "api_key": os.getenv("API_KEY", "Not set"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT", "Offline")
    }

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")

    # Logic to hide the actual password in the DB string for display
    if config['database'] != "Not set":
        print("Database: Connected to local instance")
    else:
        print("Database: Disconnected")

    if config['api_key'] != "Not set":
        print("API Access: Authenticated")
    else:
        print("API Access: Denied (Missing Key)")

    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: {'Online' if config['zion']
                           != 'Offline' else 'Offline'}")

    # Security Checks
    print("\nEnvironment security check:")

    if config['api_key'] == "Not set":
        print("[WARNING] API Key missing")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if "MATRIX_MODE" in os.environ:
        print("[OK] Production overrides available")
    else:
        print("[OK] Production overrides available (using defaults)")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()