from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import and mount the metrics API router
from src.api.metrics import router as metrics_router

app = FastAPI(
    title="App Generation Metrics API",
    version="0.1.0",
    description="""
    Backend API for serving app generation metrics data.
    ---
    - /metrics: Returns a list of app generation metric records (mock: metrics.json)
    - .env: Used to load future configuration (e.g., S3 details)
    """
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount /metrics endpoint
app.include_router(metrics_router)

@app.get("/")
def health_check():
    """Health check endpoint. Returns app status."""
    return {"message": "Healthy"}
