import importlib.util


def check_package(package_name: str) -> bool:
    """
    Checks if a package is installed and prints its version.
    Returns True if installed, False otherwise.
    """
    try:
        # We use importlib to safely check for the package without crashing
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print(f"[MISSING] {package_name}: Not found")
            return False

        # If found, we import it to get the version
        module = __import__(package_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {package_name} ({version})")
        return True
    except ImportError:
        print(f"[MISSING] {package_name}: Import failed")
        return False


def analyze_data() -> None:
    """
    Performs the matrix data analysis and visualization.
    Only runs if dependencies are present.
    """
    print("\nAnalyzing Matrix data...")

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    try:
        print("Processing 1000 data points...")
        data = {
            'power_level': np.random.normal(100, 15, 1000),
            'connection_stability': np.random.uniform(0, 1, 1000)
        }
        df = pd.DataFrame(data)

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.hist(df['power_level'], bins=30, color='green', alpha=0.7)
        plt.title('Zion Power Grid Fluctuation')
        plt.xlabel('Power Level')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)

        output_file = "matrix_analysis.png"
        plt.savefig(output_file)
        print(f"Analysis complete!\nResults saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred during analysis: {e}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    required_packages = ["pandas", "numpy", "matplotlib", "requests"]
    missing_packages = []

    print("Checking dependencies:")
    for package in required_packages:
        if not check_package(package):
            missing_packages.append(package)

    if missing_packages:
        print("\nWARNING: Critical components missing.")
        print("To load the programs, choose your method:")
        print("1. PIP (The Old Way):")
        print("   pip install -r requirements.txt")
        print("2. POETRY (The Modern Way):")
        print("   poetry install")
        print("   poetry run python loading.py")
    else:
        analyze_data()


if __name__ == "__main__":
    main()