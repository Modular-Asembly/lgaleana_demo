from typing import Any, Dict, List
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.sql_adaptor import SessionLocal, engine
from app.models.shopify_data import ShopifyData
from app.models.google_ads_data import GoogleAdsData

def get_latest_shopify_entries(session: Session, limit: int = 5) -> List[ShopifyData]:
    """
    Retrieve the latest ShopifyData entries from the database.
    
    Args:
        session (Session): SQLAlchemy database session.
        limit (int): Number of entries to retrieve.

    Returns:
        List[ShopifyData]: List of ShopifyData entries ordered by created_at descending.
    """
    return session.query(ShopifyData).order_by(desc(ShopifyData.created_at)).limit(limit).all()

def get_latest_google_ads_entries(session: Session, limit: int = 5) -> List[GoogleAdsData]:
    """
    Retrieve the latest GoogleAdsData entries from the database.
    
    Args:
        session (Session): SQLAlchemy database session.
        limit (int): Number of entries to retrieve.

    Returns:
        List[GoogleAdsData]: List of GoogleAdsData entries ordered by created_at descending.
    """
    return session.query(GoogleAdsData).order_by(desc(GoogleAdsData.created_at)).limit(limit).all()

def format_shopify_data(entries: List[ShopifyData]) -> List[Dict[str, Any]]:
    """
    Format ShopifyData entries for dashboard presentation.
    
    Args:
        entries (List[ShopifyData]): List of ShopifyData entries.

    Returns:
        List[Dict[str, Any]]: Formatted Shopify data.
    """
    formatted = []
    for entry in entries:
        formatted.append({
            "id": entry.id,
            "data": entry.data,
            "created_at": entry.created_at.isoformat()
        })
    return formatted

def format_google_ads_data(entries: List[GoogleAdsData]) -> List[Dict[str, Any]]:
    """
    Format GoogleAdsData entries for dashboard presentation.
    
    Args:
        entries (List[GoogleAdsData]): List of GoogleAdsData entries.

    Returns:
        List[Dict[str, Any]]: Formatted Google Ads data.
    """
    formatted = []
    for entry in entries:
        formatted.append({
            "id": entry.id,
            "data": entry.data,
            "created_at": entry.created_at.isoformat()
        })
    return formatted

def aggregate_dashboard_data(shopify_limit: int = 5, google_ads_limit: int = 5) -> Dict[str, Any]:
    """
    Aggregates and processes data from ShopifyData and GoogleAdsData tables.

    This function retrieves the latest entries from both tables, formats the data,
    and returns a combined dictionary ready for dashboard presentation.

    Args:
        shopify_limit (int): Number of Shopify entries to retrieve.
        google_ads_limit (int): Number of Google Ads entries to retrieve.

    Returns:
        Dict[str, Any]: Aggregated dashboard data with separate sections for each data source.
    """
    with SessionLocal() as session:
        shopify_entries = get_latest_shopify_entries(session, shopify_limit)
        google_ads_entries = get_latest_google_ads_entries(session, google_ads_limit)
    
    dashboard_data = {
        "shopify_data": format_shopify_data(shopify_entries),
        "google_ads_data": format_google_ads_data(google_ads_entries)
    }
    return dashboard_data
