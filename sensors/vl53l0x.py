import vl53l0x

from machine import Pin, I2C

from abstractions.sensor import ISensor
from constants.sensors.vl53l0x import VL53L0XConstant


class VL53L0XSensor(ISensor):
    """
    VL53L0X is a sensor for measuring distance.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
        i2c_scl: int = VL53L0XConstant.I2C_SCL,
        i2c_sda: int = VL53L0XConstant.I2C_SDA,
    ):
        """
        Initialize the VL53L0X.
        """
        super().__init__(device_urn, location_urn)

        self.i2c = I2C(scl=Pin(i2c_scl), sda=Pin(i2c_sda))
        self.sensor = vl53l0x.VL53L0X(self.i2c)
        self.sensor.set_measurement_timing_budget(
            VL53L0XConstant.MEASUREMENT_TIMING_BUDGET
        )

        print(
            f"Initializing VL53L0X for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    async def read(self) -> dict:
        """
        Read the VL53L0X.
        """
        return self.sensor.read()
