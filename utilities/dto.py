from abstractions.utility import IUtility
from dtos.abstraction import IDTO


class DTOUtility(IUtility):
    """
    DTO is a base class for all DTOs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def deserialize(self, dto: IDTO) -> str:
        """
        Serialize the DTO.
        """

        for key, value in dto.items():
            if isinstance(value, IDTO):
                dto[key] = self.serialize(value)
            elif isinstance(value, list):
                dto[key] = [self.serialize(item) for item in value]
            elif isinstance(value, dict):
                dto[key] = {k: self.serialize(v) for k, v in value.items()}

        return dto
