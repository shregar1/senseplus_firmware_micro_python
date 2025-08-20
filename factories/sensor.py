from abstractions.factory import IFactory
from constants.sensors.bh1750 import BH1750SensorConstant
from constants.sensors.bme280 import BME280SensorConstant
from constants.sensors.rtc import RTCSensorConstant
from constants.sensors.vl53l0x import VL53L0XSensorConstant
from sensors.bh1750 import BH1750Sensor
from sensors.bme280 import BME280Sensor
from sensors.rtc import RTCSensor
from sensors.vl53l0x import VL53L0XSensor


class SensorFactory(IFactory):
    """
    SensorFactory is a factory for creating sensors.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        """
        Initialize the SensorFactory.
        """
        super().__init__(device_urn, location_urn)
        self.store = {
            BH1750SensorConstant.NAME: BH1750Sensor,
            BME280SensorConstant.NAME: BME280Sensor,
            RTCSensorConstant.NAME: RTCSensor,
            VL53L0XSensorConstant.NAME: VL53L0XSensor,
        }

    def get(self, key: str) -> object:
        """
        Create a sensor.
        """

        value = self.store.get(key)

        if value is None:
            raise ValueError(f"Sensor {key} not found")

        return value
