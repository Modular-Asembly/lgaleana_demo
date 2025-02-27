from dotenv import load_dotenv
load_dotenv()  # Call load_dotenv() before any other import

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.sql_adaptor import Base, engine
from app.pull_shopify_data_endpoint import router as shopify_data_router
from app.pull_google_ads_data_endpoint import router as google_ads_router
from app.dashboard_endpoint import router as dashboard_router

def create_app() -> FastAPI:
    app = FastAPI()

    # Add CORSMiddleware with wildcard settings
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include all routers
    app.include_router(shopify_data_router)
    app.include_router(google_ads_router)
    app.include_router(dashboard_router)

    # Create all database tables
    Base.metadata.create_all(bind=engine)

    return app

app = create_app()
