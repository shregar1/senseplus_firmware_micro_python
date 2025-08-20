from dataclasses import dataclass

from dtos.measurements.abstraction import IMeasurementDTO


@dataclass
class BME280MeasurementDTO(IMeasurementDTO):
    temperature: float
    pressure: float
    humidity: float
