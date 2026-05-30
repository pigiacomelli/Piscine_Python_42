import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise RuntimeError("No data available to output.")
        return self._storage.pop(0)

    def _store(self, item: str) -> None:
        self._storage.append((self._rank, item))
        self._rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(
        self, data: int | float | list[int | float]
    ) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(
        self, data: str | list[str]
    ) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            # Casting to avoid MyPy narrowing issues with 'Any'
            d_data: dict[typing.Any, typing.Any] = data
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d_data.items()
            )
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                d_item: dict[typing.Any, typing.Any] = item
                if not all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d_item.items()
                ):
                    return False
            return True
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            if 'log_level' in d and 'log_message' in d:
                return f"{d['log_level']}: {d['log_message']}"
            return ": ".join(d.values())

        if isinstance(data, list):
            for item in data:
                self._store(format_log(item))
        else:
            self._store(format_log(data))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate('42')}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # Expected mypy warning/error to occur on the next line
        num_proc.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    print(f"Trying to validate input '42': {txt_proc.validate('42')}")
    txt_data: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {txt_data}")
    txt_proc.ingest(txt_data)
    print("Extracting 1 value...")
    rank, val = txt_proc.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
