from machine import I2C, Pin
from bme280 import BME280

from abstractions.sensor import ISensor
from constants.sensors.bme280 import BME280Constant
from dtos.measurements.bme280 import BME280Measurement


class BME280Sensor(ISensor):
    """
    BME280Sensor is a sensor for measuring temperature, humidity, and pressure.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
        i2c_scl: int = BME280Constant.I2C_SCL,
        i2c_sda: int = BME280Constant.I2C_SDA,
    ):
        """
        Initialize the BME280Sensor.
        """
        super().__init__(device_urn, location_urn)

        self.i2c = I2C(scl=Pin(i2c_scl), sda=Pin(i2c_sda))
        self.sensor = BME280(i2c=self.i2c)

        print(
            f"Initializing BME280Sensor for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    async def read(self) -> dict:
        """
        Read the BME280 sensor.
        """

        temp, pressure, humidity = self.sensor.read_compensated_data()
        return BME280Measurement(
            temperature=temp,
            pressure=pressure,
            humidity=humidity,
        )
