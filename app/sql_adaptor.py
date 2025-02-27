import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# Load environment variables as early as possible
load_dotenv()

# Retrieve the database URL from environment variables using a temporary variable
_db_url = os.getenv("DB_URL")
if not _db_url:
    raise ValueError("DB_URL environment variable is not set.")
DB_URL: str = _db_url

# Create a SQLAlchemy engine
engine = create_engine(DB_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the Base for models to inherit from
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Provides a database session that is closed after use.
    This is intended to be used as a dependency in FastAPI endpoints.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
