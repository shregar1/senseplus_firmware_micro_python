from abc import ABC, abstractmethod


class IService(ABC):
    """
    Service is a base class for all services.
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
    async def run(self) -> None:
        """
        Run the service.
        """
        pass
