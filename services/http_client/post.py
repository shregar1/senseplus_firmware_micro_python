from services.http_client.abstraction import IHTTPClientService


class HTTPClientPostService(IHTTPClientService):
    """
    HTTPClientService is a service for sending data to the cloud.
    """

    def __init__(
        self,
        device_urn: str,
        location_urn: str,
        url: str,
    ):
        super().__init__(device_urn, location_urn, url)

    async def run(
        self,
        data: dict,
        headers: dict,
    ) -> None:
        """
        Run the HTTP client service.
        """

        response = await self.request(
            url=self.url,
            data=self.data,
            headers=self.headers,
        )
        return response
