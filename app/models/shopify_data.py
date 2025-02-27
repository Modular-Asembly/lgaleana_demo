from sqlalchemy import Column, Integer, DateTime, JSON, func
from app.sql_adaptor import Base

class ShopifyData(Base):
    __tablename__ = "shopify_data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
