# metrics-dashboard-03ce4a57

## Backend API (FastAPI)
- **GET `/metrics`**: Returns list of app generation metric records (currently reads from `kavia_backend/data/metrics.json`).
  - In future, backend will support S3 (or other) storage and use `.env` variables for configuration (e.g., `S3_BUCKET`, `S3_REGION`).
- **GET `/`**: Health check endpoint.

### Metrics Data Structure
A metric record contains fields such as:
- `app_name`, `model`, `cga_version`, `start_time`, `end_time`, `duration_seconds`, `status`, `cost_usd`, `project_url`, etc.

### .env Support and Extensibility
- The backend loads environment variables from `.env` (using python-dotenv).
- No variables required for mock mode; in future, add storage/access credentials and update `metrics.py` accordingly.
