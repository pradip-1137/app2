import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
DEBUG = ENVIRONMENT == "dev"
HOST = '0.0.0.0' if ENVIRONMENT == "prod" else ''
POSTGRES_DB = os.environ.get("POSTGRES_DB", "mydb")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "pradip")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "Redhat@1137")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
