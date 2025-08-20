from dataclasses import dataclass

from dtos.measurements.abstraction import IMeasurementDTO


@dataclass
class TelemetryDTO:
    """
    TelemetryDTO is a base class for all telemetry.
    """

    start_time: str
    end_time: str
    readings: dict[str, IMeasurementDTO]
