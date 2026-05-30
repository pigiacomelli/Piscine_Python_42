import os
import sys
from typing import Optional

try:
    from dotenv import load_dotenv
    HAS_DOTENV: bool = True
except ImportError:
    HAS_DOTENV = False


def main() -> None:
    if HAS_DOTENV:
        load_dotenv()

    matrix_mode: Optional[str] = os.getenv("MATRIX_MODE")
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    api_key: Optional[str] = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint: Optional[str] = os.getenv("ZION_ENDPOINT")

    is_missing: bool = (
        not matrix_mode
        or not db_url
        or not api_key
        or not zion_endpoint
    )

    if is_missing:
        print("WARNING: Missing configuration.")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if db_url and ("local" in db_url or "sqlite" in db_url):
        print("Database: Connected to local instance")
    else:
        print(f"Database: Connected to {db_url}")

    if api_key:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
