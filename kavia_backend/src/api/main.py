from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    """Health check endpoint.
    Returns a simple healthy message.
    """
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
from typing import List
from pydantic import BaseModel, Field

class MetricRecord(BaseModel):
    """Represents a single metric record for an app generation event."""
    app_name: str = Field(..., description="Name of the generated app")
    model: str = Field(..., description="Model used for generation")
    cga_version: str = Field(..., description="CGA version")
    created_at: str = Field(..., description="ISO 8601 datetime string")
    duration_seconds: float = Field(..., description="Generation duration in seconds")
    total_cost_usd: float = Field(..., description="Total cost in USD")
    status: str = Field(..., description="Generation status (success/error)")
    project_link: str = Field(..., description="URL to generated project or artifact")

@app.get(
    "/metrics",
    response_model=List[MetricRecord],
    summary="Get app generation metric records",
    description="Returns a list of mock app generation metric records as JSON."
)
def get_metrics():
    """Returns a list of app generation metric records (mock data).

    Returns:
        List[MetricRecord]: List of app generation metric records.
    """
    return [
        {
            "app_name": "SalesDashboard",
            "model": "gpt-4",
            "cga_version": "1.2.0",
            "created_at": "2024-07-04T13:22:11Z",
            "duration_seconds": 68.2,
            "total_cost_usd": 2.45,
            "status": "success",
            "project_link": "https://example.com/artifacts/SalesDashboard"
        },
        {
            "app_name": "InventoryManager",
            "model": "gpt-4",
            "cga_version": "1.1.3",
            "created_at": "2024-07-02T09:17:44Z",
            "duration_seconds": 55.4,
            "total_cost_usd": 1.98,
            "status": "success",
            "project_link": "https://example.com/artifacts/InventoryManager"
        },
        {
            "app_name": "AIContentWriter",
            "model": "gpt-3.5-turbo",
            "cga_version": "1.0.9",
            "created_at": "2024-07-01T16:03:29Z",
            "duration_seconds": 87.6,
            "total_cost_usd": 3.27,
            "status": "error",
            "project_link": "https://example.com/artifacts/AIContentWriter"
        }
    ]
