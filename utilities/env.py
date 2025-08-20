from abstractions.utility import IUtility


class EnvUtility(IUtility):
    """
    EnvUtility is a utility for managing environment variables.
    """

    def __init__(
        self,
        device_urn: str = None,
        location_urn: str = None,
    ):
        """
        Initialize the EnvUtility.
        """
        self.device_urn = device_urn
        self.location_urn = location_urn

        print(
            f"Initializing EnvUtility for "
            f"{self.device_urn} at {self.location_urn}..."
        )

    def load_env(self, path: str = ".env") -> dict[str, str]:
        """
        Load the environment variables from the .env file.
        """

        env = {}
        try:
            print(f"Loading environment variables from {path}...")
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    key, value = line.split("=", 1)
                    env[key.strip()] = value.strip()
            print(f"Loaded {len(env)} environment variables")
            return env

        except Exception as e:
            print(f"Could not read .env: {str(e)}")
            raise e
