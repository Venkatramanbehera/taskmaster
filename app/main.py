from fastapi import FastAPI, status
from app.api.v1.endpoints import router as task_router

app = FastAPI(
    title="My Versioned API",
    description="Example demonstrating modular API versioning in FastAPI"
)

app.include_router(task_router, prefix="/v1", tags=["tasks"])

@app.get('/health', status_code= 200)
def health():
    return "OK"