from dotenv import load_dotenv
import os

load_dotenv()

_database_url = os.getenv("DATABASE_URL")

if _database_url is None:
    raise ValueError("DATABASE_URL is not set")

DATABASE_URL: str = _database_url