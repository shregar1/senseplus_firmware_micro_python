import json

from abc import ABC, abstractmethod


class IConfiguration(ABC):
    """
    IConfiguration is a base class for all configurations.
    """

    config = None

    @abstractmethod
    def __init__(self) -> object:
        """
        Initialize the configuration.
        """
        pass

    def load(self) -> dict:
        """
        Load the configuration from JSON file.
        Default implementation for all configurations.
        """
        try:
            with open(self.path, "r") as file:
                config: dict = json.load(file)
            return config
        except FileNotFoundError:
            print(f"Configuration file not found: {self.path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in configuration file {self.path}: {e}")
            return {}

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of SensorConfiguration.
        """
        pass
