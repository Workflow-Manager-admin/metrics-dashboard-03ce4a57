"""
metrics.py

Implements the /metrics endpoint for the FastAPI backend.

- Currently serves mock metrics data loaded from a local JSON file in the data/ directory.
- Structured for easy replacement of the local data loader with S3 or other cloud providers in the future.
- Uses python-dotenv for .env expansion (expected practice for config; not required for the mock version, but demonstration included).

PUBLIC_INTERFACE:
    - GET /metrics: Returns a list of metric records (JSON).

ENVIRONMENT:
    - Metrics data source location/config to be set via .env variables (e.g., S3_BUCKET, S3_REGION) in future implementations.
    - Current: Uses ./data/metrics.json.
"""

from pathlib import Path
from typing import List, Any

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

# .env loading for future extensibility (not strictly required for mock)
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from .env if present

router = APIRouter()

# Path to mock data (for development/testing)
DEFAULT_DATA_PATH = Path(__file__).parent.parent / "data" / "metrics.json"

def load_mock_metrics(data_path: Path = DEFAULT_DATA_PATH) -> List[Any]:
    """Loads the mock metrics data from a local JSON file."""
    import json

    if not data_path.exists():
        # If no mock data file is present, return an empty list or raise an error
        raise HTTPException(status_code=404, detail="Mock metrics data file not found")
    with open(data_path, "r") as f:
        return json.load(f)

# PUBLIC_INTERFACE
@router.get("/metrics", response_class=JSONResponse, tags=["Metrics"])
async def get_metrics():
    """
    Returns list of app generation metric records.

    Returns:
        List of dictionaries, each representing an app generation metric record.
    ---
    Future Expansion Notes:
        - To switch to S3 or another backend, replace `load_mock_metrics` with a loader using env variables.
    """
    try:
        metrics = load_mock_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to load metrics: {str(e)}")
