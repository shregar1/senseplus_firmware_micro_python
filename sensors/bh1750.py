import bh1750

from machine import I2C, Pin

from abstractions.sensor import ISensor
from constants.sensors.bh1750 import BH1750Constant
from dtos.measurements.bh1750 import BH1750Measurement


class BH1750Sensor(ISensor):
    """
    BH1750Sensor is a sensor for measuring light intensity.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
        i2c_scl: int = BH1750Constant.I2C_SCL,
        i2c_sda: int = BH1750Constant.I2C_SDA,
    ):
        super().__init__(device_urn, location_urn)

        self.i2c = I2C(scl=Pin(i2c_scl), sda=Pin(i2c_sda))
        self.sensor = bh1750.BH1750(self.i2c)

        print(
            f"Initializing BH1750Sensor for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    async def read(self) -> dict:
        """
        Read the BH1750 sensor.
        """

        lux: float = self.sensor.luminance(bh1750.BH1750.ONCE_HIRES_1)
        return BH1750Measurement(
            lux=lux
        )
