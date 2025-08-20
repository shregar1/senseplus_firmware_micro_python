from abstractions.configuration import IConfiguration
from dtos.configurations.sensor import SensorConfigurationDTO


class SensorConfiguration(IConfiguration):
    """
    SensorConfiguration is a configuration for the sensor.
    Implements singleton pattern to ensure only one instance exists.
    """

    _instance: "SensorConfiguration" = None
    _config_data: SensorConfigurationDTO = None

    def __new__(cls):
        """
        Singleton pattern implementation using __new__.
        Ensures only one instance of SensorConfiguration exists.
        """
        if cls._instance is None:
            cls._instance = super(SensorConfiguration, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> object:
        # Only initialize once
        if self._instance is None:
            super().__init__()
            self.path = "configs/sensor/config.json"
            self.config = None

    def get_instance(self) -> object:
        """
        Get a configuration value or the entire configuration.

        Args:
            key: Optional key to get specific value.
            If None, returns entire config.

        Returns:
            Configuration value(s) as SensorConfigurationDTO or specific value.
        """
        if self._instance is None:
            config_dict = self.load()
            self.config = SensorConfigurationDTO(
                include=config_dict.get("include", [])
            )
        return self._instance.config
