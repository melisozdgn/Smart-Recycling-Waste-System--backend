# fastapi_ai/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import classify

app = FastAPI(
    title="SRWS AI Service",
    description="Smart Waste Sorting System — AI Classification Microservice",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classify.router, prefix="/api/ai", tags=["AI Classification"])

@app.get("/health")
async def health():
    return {"status": "ok", "service": "SRWS AI"}
