from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.sql_adaptor import get_db
from app.models.google_ads_data import GoogleAdsData
from app.google_ads_service import fetch_and_process_google_ads_data

router: APIRouter = APIRouter()

@router.post("/pull-google-ads-data", summary="Pull Google Ads Data")
def pull_google_ads_data(db: Session = Depends(get_db)) -> dict:
    processed_data: dict = fetch_and_process_google_ads_data()
    new_data = GoogleAdsData(data=processed_data)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status": "success", "id": new_data.id}
