from dataclasses import dataclass

from dtos.measurements.abstraction import IMeasurementDTO


@dataclass
class VL53L0XMeasurementDTO(IMeasurementDTO):
    distance: float
