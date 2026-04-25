# loading.py

import sys
import importlib


REQUIRED_LIBS = ["pandas", "numpy", "matplotlib", "requests"]


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    available = {}
    missing = []

    for lib in REQUIRED_LIBS:
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - ready")
            available[lib] = module
        except ImportError:
            print(f"[MISSING] {lib} - not installed")
            missing.append(lib)

    if missing:
        print("\nMissing dependencies detected.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        return None

    return available


def analyze_data(mods):
    np = mods["numpy"]
    pd = mods["pandas"]
    plt = mods["matplotlib"].pyplot

    print("\nAnalyzing Matrix data...")

    # Generate data with numpy (required constraint)
    data = np.random.normal(loc=0, scale=1, size=1000)

    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame({"signal": data})
    df["smoothed"] = df["signal"].rolling(window=10).mean()

    print("Generating visualization...")

    plt.figure()
    plt.plot(df["signal"])
    plt.plot(df["smoothed"])
    plt.title("Matrix Signal Analysis")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    mods = check_dependencies()

    if not mods:
        return

    # Lazy import matplotlib.pyplot to avoid import errors early
    try:
        import matplotlib.pyplot as plt
        mods["matplotlib"].pyplot = plt
    except ImportError:
        print("[ERROR] matplotlib.pyplot not available")
        return

    analyze_data(mods)


if __name__ == "__main__":
    main()