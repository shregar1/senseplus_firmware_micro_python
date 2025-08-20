from dataclasses import dataclass

from dtos.measurements.abstraction import IMeasurementDTO


@dataclass
class BH1750MeasurementDTO(IMeasurementDTO):
    lux: float
