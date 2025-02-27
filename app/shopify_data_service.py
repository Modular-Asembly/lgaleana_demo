import os
from typing import Any, Dict

from dotenv import load_dotenv
from app.shopify_api_client import fetch_dummy_shopify_data

# Load environment variables as early as possible
load_dotenv()

SHOPIFY_API_KEY: str = os.getenv("SHOPIFY_API_KEY", "")
SHOPIFY_PASSWORD: str = os.getenv("SHOPIFY_PASSWORD", "")
SHOPIFY_STORE_URL: str = os.getenv("SHOPIFY_STORE_URL", "")

if not all([SHOPIFY_API_KEY, SHOPIFY_PASSWORD, SHOPIFY_STORE_URL]):
    raise ValueError("One or more required Shopify environment variables are not set.")

def fetch_and_process_shopify_data() -> Dict[str, Any]:
    """
    Fetches raw data from the Shopify API client, processes it by incorporating Shopify credentials,
    and prepares it for persistence in the ShopifyData table.

    Returns:
        Dict[str, Any]: Processed Shopify data ready for model insertion.
    """
    # Fetch raw data from the Shopify API client module
    raw_data: Dict[str, Any] = fetch_dummy_shopify_data()
    
    # Process the raw data by appending Shopify credentials
    processed_data: Dict[str, Any] = {
        "api_key": SHOPIFY_API_KEY,
        "password": SHOPIFY_PASSWORD,
        "store_url": SHOPIFY_STORE_URL,
        "raw": raw_data
    }
    
    return processed_data
