from abstractions.sensor import ISensor
from abstractions.service import IService
from configurations.sensor import SensorConfiguration
from constants.sensors.abstraction import ISensorConstant
from constants.sensors.rtc import RTCSensorConstant
from dtos.configurations.sensor import SensorConfigurationDTO
from dtos.measurements.abstraction import IMeasurement
from dtos.services.telemetry import TelemetryDTO
from factories.sensor import SensorFactory
from sensors.rtc import RTCSensor


class TelemetryService(IService):
    """
    TelemetryService is a service for sending telemetry data to the cloud.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        """
        Initialize the TelemetryService.
        """
        super().__init__(device_urn, location_urn)
        self.sensor_configuration = SensorConfiguration.get_instance()

    async def run(self) -> None:
        """
        Run the TelemetryService.
        """
        sensor_configuration: SensorConfigurationDTO = (
            SensorConfiguration.get_instance()
        )

        rtc_sensor: RTCSensor = SensorFactory.get(RTCSensorConstant.NAME)(
            device_urn=self.device_urn,
            location_urn=self.location_urn,
        )

        telemetry_data: dict[str, IMeasurement] = dict()
        for sensor_name in sensor_configuration.include:

            start_time = await rtc_sensor.read()

            sensor: ISensor = SensorFactory.get(sensor_name)(
                device_urn=self.device_urn,
                location_urn=self.location_urn,
                i2c_scl=ISensorConstant.I2C_SCL,
                i2c_sda=ISensorConstant.I2C_SDA,
            )
            measurement_dto: IMeasurement = await sensor.read()

            telemetry_data.update({
                sensor_name: measurement_dto
            })

            end_time = await rtc_sensor.read()

        return TelemetryDTO(
            start_time=start_time,
            end_time=end_time,
            readings=telemetry_data,
        )
