# data_pipeline.py

from typing import Protocol, List, Tuple
from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
from ex1.data_stream import DataStream


# ================= EXPORT PROTOCOL =================

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


# ================= CSV PLUGIN =================

class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


# ================= JSON PLUGIN =================

class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        items = []
        for idx, value in data:
            items.append(f'"item_{idx}": "{value}"')
        print("{" + ", ".join(items) + "}")


# ================= EXTENDED DATASTREAM =================

class PipelineDataStream(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted = []

            for _ in range(nb):
                if len(proc._data) == 0:
                    break
                extracted.append(proc.output())

            if extracted:
                plugin.process_output(extracted)


# ================= TEST =================

if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("Initialize Data Stream...")
    ds = PipelineDataStream()
    ds.print_processors_stats()

    # Register processors
    print("Registering Processors")
    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    ds.register_processor(num)
    ds.register_processor(txt)
    ds.register_processor(log)

    # First batch
    stream1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", stream1)
    ds.process_stream(stream1)
    ds.print_processors_stats()

    # CSV export
    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    # Second batch
    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data:", stream2)
    ds.process_stream(stream2)
    ds.print_processors_stats()

    # JSON export
    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()