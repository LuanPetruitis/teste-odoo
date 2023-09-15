from os import getenv

# Database
MONGO_URL: str = getenv("MONGO_URL", "mongodb")
DATABASE_ENVIRONMENT: str = getenv("DATABASE_ENVIRONMENT", "flash_desenvolvimento")
