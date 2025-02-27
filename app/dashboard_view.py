from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.dashboard_service import aggregate_dashboard_data

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard")
async def dashboard_view(request: Request):
    """
    Retrieves aggregated dashboard data for both Shopify and Google Ads,
    and renders the dashboard template with the fetched data.
    """
    dashboard_data = aggregate_dashboard_data()
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": dashboard_data})
