from typing import Any, Dict

def fetch_dummy_google_ads_data() -> Dict[str, Any]:
    """
    Simulates fetching raw data from the Google Ads API.
    Returns dummy data representing a typical Google Ads API response.
    """
    dummy_response: Dict[str, Any] = {
        "campaigns": [
            {
                "campaign_id": 987654321,
                "name": "Dummy Campaign 1",
                "status": "enabled",
                "metrics": {
                    "clicks": 120,
                    "impressions": 5000,
                    "cost": 150.75
                }
            },
            {
                "campaign_id": 123456789,
                "name": "Dummy Campaign 2",
                "status": "paused",
                "metrics": {
                    "clicks": 85,
                    "impressions": 4200,
                    "cost": 98.50
                }
            }
        ],
        "account": {
            "account_id": 1122334455,
            "currency": "USD",
            "timezone": "America/New_York"
        }
    }
    return dummy_response
