import network
import time

from abstractions.utility import IUtility


class WifiUtility(IUtility):
    """
    Wifi is a utility for managing WiFi connections.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
        ssid: str = None,
        password: str = None,
    ):
        """
        Initialize the WifiUtility.
        """

        super().__init__(device_urn, location_urn)

        if ssid is None or password is None:
            raise ValueError("SSID and password are required")
        else:
            self.ssid = ssid
            self.password = password

        print(
            f"Initializing WifiUtility for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    def connect(self) -> network.WLAN:
        """
        Connect to the WiFi network.
        """

        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        retry_count = 0
        while not self.wlan.isconnected() and retry_count < 20:
            print(f"Connecting to {self.ssid}... ({retry_count}/20)")
            time.sleep(1)
            retry_count += 1
        if retry_count == 20:
            print(f"Failed to connect to {self.ssid}")
            return None
        else:
            print(f"Connected to {self.ssid}")
            return self.wlan

    def disconnect(self) -> None:
        """
        Disconnect from the WiFi network.
        """

        self.wlan.disconnect()
        self.wlan.active(False)

    def get_status(self) -> bool:
        """
        Get the status of the WiFi connection.
        """

        return self.wlan.isconnected()
