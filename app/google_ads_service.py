import os
from typing import Any, Dict

from dotenv import load_dotenv
from app.google_ads_api_client import fetch_dummy_google_ads_data

# Load environment variables as early as possible
load_dotenv()

GOOGLE_ADS_CLIENT_ID: str = os.getenv("GOOGLE_ADS_CLIENT_ID", "")
GOOGLE_ADS_CLIENT_SECRET: str = os.getenv("GOOGLE_ADS_CLIENT_SECRET", "")
GOOGLE_ADS_DEVELOPER_TOKEN: str = os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN", "")
GOOGLE_ADS_REFRESH_TOKEN: str = os.getenv("GOOGLE_ADS_REFRESH_TOKEN", "")

if not all([GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_REFRESH_TOKEN]):
    raise ValueError("One or more Google Ads environment variables are not set.")

def fetch_and_process_google_ads_data() -> Dict[str, Any]:
    """
    Fetches data from the Google Ads API client, processes the data, and prepares it for persistence.

    Returns:
        Dict[str, Any]: Processed Google Ads data ready for model insertion.
    """
    # Fetch raw data from the Google Ads API client
    raw_data: Dict[str, Any] = fetch_dummy_google_ads_data()
    
    # Process raw data by adding developer credentials info if needed
    processed_data: Dict[str, Any] = {
        "client_id": GOOGLE_ADS_CLIENT_ID,
        "client_secret": GOOGLE_ADS_CLIENT_SECRET,
        "developer_token": GOOGLE_ADS_DEVELOPER_TOKEN,
        "refresh_token": GOOGLE_ADS_REFRESH_TOKEN,
        "raw": raw_data
    }
    return processed_data
