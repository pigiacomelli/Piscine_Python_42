from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data.
        Must be implemented by subclasses.
        """
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Default filtering: if no criteria, return all data.
        Subclasses may override.
        """
        if criteria is None:
            return data_batch

        # Simple default filter: keep items containing criteria (string match)
        filtered = []
        for item in data_batch:
            if criteria in str(item):
                filtered.append(item)

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Default statistics.
        Subclasses may extend this.
        """
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }
