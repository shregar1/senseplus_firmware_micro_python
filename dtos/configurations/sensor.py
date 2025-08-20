from dataclasses import dataclass


@dataclass
class SensorConfigurationDTO:
    """
    SensorConfiguration is a configuration for the sensor.
    """

    include: list[str]
