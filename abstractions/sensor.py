from abc import ABC, abstractmethod


class ISensor(ABC):
    """
    Sensor is a base class for all sensors.
    """

    @abstractmethod
    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        self.device_urn = device_urn
        self.location_urn = location_urn

    @abstractmethod
    async def read(self) -> dict:
        pass
