# data_stream.py

from typing import Any, List
from ex0.data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


class DataStream:
    def __init__(self):
        self._processors: List[DataProcessor] = []
        self._processed_count: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._processed_count[proc] = 0

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    # count items correctly (list vs single)
                    if isinstance(element, list):
                        self._processed_count[proc] += len(element)
                    else:
                        self._processed_count[proc] += 1
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = self._processed_count.get(proc, 0)
            remaining = len(proc._data)  # internal queue size
            print(f"{name}: total {total} items processed, remaining {remaining} on processor")


# ================= TEST =================

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    # Create processors
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    # Stream data
    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    # First phase
    print()
    print("Registering Numeric Processor")
    print()
    ds.register_processor(num_proc)

    print("Send first batch of data on stream:", stream)
    ds.process_stream(stream)
    ds.print_processors_stats()

    # Register remaining processors
    print()
    print("Registering other data processors")
    ds.register_processor(txt_proc)
    ds.register_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()

    # Consume data
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")

    for _ in range(3):
        num_proc.output()

    for _ in range(2):
        txt_proc.output()

    for _ in range(1):
        log_proc.output()

    ds.print_processors_stats()