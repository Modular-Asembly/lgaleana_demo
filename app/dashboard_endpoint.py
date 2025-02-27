from typing import Any, Dict
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.dashboard_service import aggregate_dashboard_data

router: APIRouter = APIRouter()
templates: Jinja2Templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard")
async def dashboard_view(request: Request) -> Any:
    """
    Retrieves aggregated dashboard data from both ShopifyData and GoogleAdsData tables
    and renders it using the dashboard Jinja2 template.
    """
    dashboard_data: Dict[str, Any] = aggregate_dashboard_data()
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": dashboard_data})
