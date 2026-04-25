# data_processor.py

from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data to output")
        item = self._data.pop(0)
        return item


# ================= NUMERIC =================

NumericType = Union[int, float]
NumericInput = Union[NumericType, List[NumericType]]


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: NumericInput) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for value in data:
                self._data.append((self._counter, str(value)))
                self._counter += 1
        else:
            self._data.append((self._counter, str(data)))
            self._counter += 1


# ================= TEXT =================

TextInput = Union[str, List[str]]


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: TextInput) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for value in data:
                self._data.append((self._counter, value))
                self._counter += 1
        else:
            self._data.append((self._counter, data))
            self._counter += 1


# ================= LOG =================

LogType = Dict[str, str]
LogInput = Union[LogType, List[LogType]]


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d):
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list) and all(is_valid_log(x) for x in data):
            return True
        return False

    def ingest(self, data: LogInput) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d: Dict[str, str]) -> str:
            return f"{d.get('log_level', '')}: {d.get('log_message', '')}"

        if isinstance(data, list):
            for entry in data:
                self._data.append((self._counter, format_log(entry)))
                self._counter += 1
        else:
            self._data.append((self._counter, format_log(data)))
            self._counter += 1


# ================= TEST =================

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()
    # Numeric
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print("Trying to validate input '42':", np.validate(42))
    print("Trying to validate input 'Hello':", np.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except Exception as e:
        print("Got exception:", e)

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for _ in range(3):
        idx, val = np.output()
        print(f"Numeric value {idx}: {val}")

    # Text
    print()
    print("Testing Text Processor...")
    tp = TextProcessor()
    print("Trying to validate input '42':", tp.validate(42))

    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(['Hello', 'Nexus', 'World'])

    print("Extracting 1 value...")
    idx, val = tp.output()
    print(f"Text value {idx}: {val}")

    # Log
    print()
    print("Testing Log Processor...")
    lp = LogProcessor()
    print("Trying to validate input 'Hello':", lp.validate("Hello"))

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    print("Processing data:", logs)
    lp.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        idx, val = lp.output()
        print(f"Log entry {idx}: {val}")