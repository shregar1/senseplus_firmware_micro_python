from abc import ABC, abstractmethod


class IFactory(ABC):
    """
    Factory is a base class for all factories.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        """
        Initialize the Factory.
        """
        self.device_urn = device_urn
        self.location_urn = location_urn

    @abstractmethod
    def create(self, *args, **kwargs) -> object:
        """
        Create an object.
        """
        pass
