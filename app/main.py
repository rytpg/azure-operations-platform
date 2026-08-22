import os
import logging
from datetime import UTC, datetime
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


APP_VERSION = "0.1.2"
APP_ENVIRONMENT = os.getenv("APP_ENV", "local")

app = FastAPI(
    title = "Azure Operations Platform",
    description = "A small service status API for demonstrating cloud operations",
    version = APP_VERSION,
)

@app.get("/")
def read_root() -> dict[str,str]:
    return{
        "message": "Azure Operations Platform",
        "documentation": "/docs"
    }

@app.get("/health")
def health_check() -> dict[str,str]:
    logger.info("Health check requested")
    return{
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat()
    }

@app.get("/services")
def list_services() -> list[dict[str,str]]:
    return [
        {
            "name": "customer-api",
            "status": "operational"
        },
        {
            "name": "identity-service",
            "status": "operational"
        },
        {
            "name": "storage-service",
            "status": "operational"
        }
    ]

@app.get("/version")
def get_version() -> dict[str,str]:
    return {
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
    }