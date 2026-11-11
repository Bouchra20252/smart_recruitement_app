from fastapi import FastAPI

from app.routes.cv_routes import router as cv_router

app = FastAPI(
    title="Smart Recruitment API",
    description="AI-powered recruitment and job matching platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Recruitment API",
        "status": "Running"
    }


app.include_router(cv_router, tags=["CV Management"])