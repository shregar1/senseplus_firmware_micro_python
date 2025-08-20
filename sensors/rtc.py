import machine

from abstractions.sensor import ISensor
from dtos.measurements.rtc import RTCMeasurement


class RTCSensor(ISensor):
    """
    RTC is a sensor for measuring time.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        """
        Initialize the RTC.
        """
        super().__init__(device_urn, location_urn)

        self.rtc = machine.RTC()

        print(
            f"Initializing RTC for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    def set(
        self,
        datetime: tuple[int, int, int, int, int, int, int, int],
    ) -> bool:
        """
        Set the RTC.
        """
        try:

            self.rtc.datetime(datetime)
            print(f"RTC set to: {datetime}")
            return True

        except Exception as e:
            print(f"Error setting RTC: {e}")
            print(f"Time tuple: {"-".join(str(x) for x in datetime)}")
            return False

    def read(self) -> RTCMeasurement:
        """
        Get the RTC.
        """
        datetime = self.rtc.datetime()
        return RTCMeasurement(
            year=datetime[0],
            month=datetime[1],
            day=datetime[2],
            hour=datetime[4],
            minute=datetime[5],
            second=datetime[6],
            weekday=datetime[3],
            yearday=datetime[7],
        )
