from abc import ABC, abstractmethod
from ast import Dict


class IDTO(ABC, Dict):
    """
    IDTO is a base class for all DTOs.
    """

    @abstractmethod
    def model_dump(self) -> dict:
        """
        Return the DTO as a dictionary.
        """
        return self.dict()
