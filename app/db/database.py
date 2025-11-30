import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,            # shows SQL in terminal (you can turn off later)
    future=True
)

# SessionLocal gives us DB sessions per request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base will be used for models
Base = declarative_base()

