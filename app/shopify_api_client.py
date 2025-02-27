from typing import Any, Dict

def fetch_dummy_shopify_data() -> Dict[str, Any]:
    """
    Simulates fetching raw data from Shopify API.
    Returns dummy data representing a typical response.
    """
    # Dummy data simulating a response from Shopify API
    dummy_response: Dict[str, Any] = {
        "shop": {
            "id": 123456789,
            "name": "Dummy Store",
            "email": "contact@dummyshop.com",
            "domain": "dummyshop.myshopify.com"
        },
        "orders": [
            {
                "order_id": 1,
                "total": 59.99,
                "currency": "USD",
                "items": [
                    {"id": 101, "name": "Item A", "quantity": 1, "price": 59.99}
                ]
            },
            {
                "order_id": 2,
                "total": 89.99,
                "currency": "USD",
                "items": [
                    {"id": 102, "name": "Item B", "quantity": 2, "price": 44.99}
                ]
            }
        ]
    }
    return dummy_response
