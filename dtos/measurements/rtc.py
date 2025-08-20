from dataclasses import dataclass

from dtos.measurements.abstraction import IMeasurementDTO


@dataclass
class RTCMeasurementDTO(IMeasurementDTO):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    weekday: int
    yearday: int
