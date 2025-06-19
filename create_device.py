from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    Entity,
)
from dotenv import load_dotenv
import os 

## Some documentation can be found here https://pypi.org/project/netboxlabs-diode-sdk/

# Load environment variables from .env file
load_dotenv()


# Step 1: Define the connection parameters
NETBOX_SERVER = os.getenv("NETBOX_URL", "http://localhost:8000")  # replace with your NetBox URL
DIODE_SERVER = os.getenv("DIODE_SERVER", "grpc://localhost:8080/diode")  # or your deployed Diode endpoint
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN",  "your_netbox_token_here")  # replace with your NetBox API token
DIODE_API_KEY = os.getenv("DIODE_API_KEY", "your_diode_api_key_here")  # replace with your Diode API key

print(f"Connecting to Diode at {DIODE_SERVER} with API key {DIODE_API_KEY}")

def main():
    with DiodeClient(
        target=DIODE_SERVER,
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Ingest device with device type, platform, manufacturer, site, role, and tags.
        """

        device = Device(
            name="Device A",
            device_type="Device Type A",
            platform="Platform A",
            manufacturer="Manufacturer A",
            site="Site ABC",
            role="Role ABC",
            serial="123456",
            asset_tag="123456",
            status="active",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device=device))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()
