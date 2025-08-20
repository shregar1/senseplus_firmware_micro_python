import network
import time

from abstractions.pipeline import IPipeline
from dtos.services.telemetry import TelemetryDTO
from services.http_client.post import HTTPClientPostService
from services.telemetry import TelemetryService
from utilities.dto import DTOUtility


class RemoteSensingStartPipeline(IPipeline):
    """
    RemoteSensingStartPipeline is a pipeline for starting the remote sensing.
    """

    def __init__(
        self,
        device_urn: str,
        location_urn: str,
        wlan: network.WLAN,
    ):
        """
        Initialize the RemoteSensingStartPipeline.
        """
        super().__init__(device_urn, location_urn)
        self.wlan: network.WLAN = wlan
        self.dto_utility: DTOUtility = DTOUtility()

    async def execute(self) -> None:
        """
        Execute the pipeline.
        """

        service = TelemetryService(
            device_urn=self.device_urn,
            location_urn=self.location_urn,
        )

        url = "http://localhost:8000/api/v1/telemetry/create"

        http_client_service = HTTPClientPostService(
            device_urn=self.device_urn,
            location_urn=self.location_urn,
            url=url,
        )

        while True:

            telemetry_dto: TelemetryDTO = await service.run()            
            _ = await http_client_service.run(
                data=self.dto_utility.deserialize(telemetry_dto),
                headers={},
            )

            time.sleep(1)

        return None
