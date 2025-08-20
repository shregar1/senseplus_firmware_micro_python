from abc import ABC, abstractmethod


class IPipeline(ABC):
    """
    IPipeline is a base class for all pipelines.
    """

    @abstractmethod
    def __init__(self, device_urn: str, location_urn: str):
        self.device_urn = device_urn
        self.location_urn = location_urn

    @abstractmethod
    async def execute(self) -> None:
        """
        Run the pipeline.
        """
        pass
