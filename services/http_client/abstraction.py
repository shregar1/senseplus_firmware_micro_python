import urequests
from abstractions.service import IService


class IHTTPClientService(IService):
    """
    IHTTPClientService is a base class for all HTTP client services.
    """

    def __init__(
        self,
        device_urn: str,
        location_urn: str,
        url: str,
    ):
        super().__init__(device_urn, location_urn)
        self.url = url

    async def request(
        self,
        url: str,
        data: dict,
        headers: dict,
    ) -> dict:
        """
        Send data to the cloud.
        """

        response = urequests.post(
            url=url,
            json=data,
            headers=headers,
        )
        return response.json()

    async def run(self) -> None:
        """
        Run the HTTP client service.
        """
        pass
