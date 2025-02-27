from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.sql_adaptor import get_db
from app.models.shopify_data import ShopifyData
from app.shopify_data_service import fetch_and_process_shopify_data

router: APIRouter = APIRouter()

@router.post("/pull-shopify-data", summary="Pull Shopify Data")
def pull_shopify_data(db: Session = Depends(get_db)) -> dict:
    processed_data: dict = fetch_and_process_shopify_data()
    new_data = ShopifyData(data=processed_data)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status": "success", "id": new_data.id}
