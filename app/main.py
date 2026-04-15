
from fastapi import FastAPI
from app.database import client

app = FastAPI(
    title="Social Media API",
    description="A REST API for social media built with FastAPI and MongoDB",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_db():
    try:
        await client.admin.command('ping')
        print("Connected to MongoDB successfully")
    except Exception as e:
        print(f"Could not connect to MongoDB: {e}")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Server is running"
    }