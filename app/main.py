
from fastapi import FastAPI

app = FastAPI(
    title="Social Media API",
    description="A REST API for social media",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Server is running"
    }