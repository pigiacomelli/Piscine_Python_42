import sys
import importlib
from typing import Dict, Tuple

REQUIRED_PACKAGES = ['pandas', 'numpy', 'requests', 'matplotlib']


def check_package_version(package_name: str) -> Tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, 'not installed'


def get_description(package_name: str) -> str:
    descriptions = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'requests': 'Network access ready',
        'matplotlib': 'Visualization ready'
    }
    return descriptions.get(package_name, 'Ready')


def display_dependencies() -> Dict[str, Tuple[bool, str]]:
    print("Checking dependencies:")
    deps = {}
    for package in REQUIRED_PACKAGES:
        available, version = check_package_version(package)
        deps[package] = (available, version)

        if available:
            description = get_description(package)
            print(f"[OK] {package} ({version}) - {description}")
        else:
            print(f"[FAIL] {package} ({version})")

    return deps


def install_instructions() -> None:
    print()
    print("To install dependencies:")
    print()
    print("Using pip:")
    print("pip install -r requirements.txt")
    print()
    print("Using Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def analyze_matrix_data() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")

        matrix_data = np.random.normal(loc=100, scale=15, size=1000)
        df = pd.DataFrame({'values': matrix_data})

        print(f"Processing {len(df)} data points...")
        print("Generating visualization...\n")

        plt.figure(figsize=(10, 6))
        plt.hist(df['values'], bins=50, edgecolor='black', alpha=0.7)
        plt.title('Matrix Data Distribution')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        plt.savefig('matrix_analysis.png', dpi=100, bbox_inches='tight')
        plt.close()

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except ImportError as e:
        print()
        print(f"Cannot proceed: {e}")
        install_instructions()
        sys.exit(1)


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print()

    deps = display_dependencies()

    required_available = all(
        deps[pkg][0] for pkg in ['pandas', 'numpy', 'matplotlib']
    )

    if not required_available:
        install_instructions()
        sys.exit(1)

    print()
    analyze_matrix_data()


if __name__ == "__main__":
    main()
