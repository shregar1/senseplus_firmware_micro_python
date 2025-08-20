from abc import ABC, abstractmethod


class IUtility(ABC):
    """
    Utility is a base class for all utilities.
    """

    @abstractmethod
    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        self.device_urn = device_urn
        self.location_urn = location_urn
