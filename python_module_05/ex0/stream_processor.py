from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return False

        for item in data:
            if type(item) not in (int, float):
                return False

        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data provided.")

        count = 0
        total = 0.0

        for item in data:
            total += item
            count += 1

        if count > 0:
            average = total / count
        else:
            average = 0.0

        result = f"Processed {count} numeric values, sum={total}, avg={average}"
        return self.format_output(result)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return type(data) is str

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data provided.")

        char_count = 0
        word_count = 0
        in_word = False

        for char in data:
            char_count += 1

            if char != ' ' and not in_word:
                word_count += 1
                in_word = True
            elif char == ' ':
                in_word = False

        result = f"Processed text: {char_count} characters, {word_count} words"
        return self.format_output(result)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False

        if ":" not in data:
            return False

        level, message = data.split(":", 1)

        if not level.strip() or not message.strip():
            return False

        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry provided.")

        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()

        if level == "ERROR":
            prefix = "[ALERT]"
        elif level == "WARNING":
            prefix = "[WARNING]"
        elif level == "INFO":
            prefix = "[INFO]"
        else:
            prefix = "[LOG]"

        result = f"{prefix} {level} level detected: {message}"
        return self.format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    # Numeric Processor
    numeric_processor = NumericProcessor()
    print("\nInitializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]

    print(f"Processing data: {numeric_data}")
    if numeric_processor.validate(numeric_data):
        print("Validation: Numeric data verified")
        print(numeric_processor.process(numeric_data))
    else:
        print("Validation failed")

    # Text Processor
    text_processor = TextProcessor()
    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"

    print(f'Processing data: "{text_data}"')
    if text_processor.validate(text_data):
        print("Validation: Text data verified")
        print(text_processor.process(text_data))
    else:
        print("Validation failed")

    # Log Processor
    log_processor = LogProcessor()
    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"

    print(f'Processing data: "{log_data}"')
    if log_processor.validate(log_data):
        print("Validation: Log entry verified")
        print(log_processor.process(log_data))
    else:
        print("Validation failed")

    # Polymorphic Demo
    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    index = 1
    for processor, data in zip(processors, data_samples):
        try:
            result = processor.process(data)
            print(f"Result {index}: {result}")
        except ValueError as e:
            print(f"Result {index}: Error - {e}")
        index += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
