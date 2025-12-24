from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.core.config import settings
from src.core.logger import get_logger

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} in {settings.ENVIRONMENT} mode")
    yield
    logger.info("Shutting down application...")

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    logger.debug("Health check requested")
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.ENVIRONMENT
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the GenAI MLOps Platform API"}

@app.post("/generate")
async def generate_text(prompt: str):
    logger.info(f"Received generation request for prompt length: {len(prompt)}")
    return {
        "response": f"Mock response for: {prompt}",
        "model": settings.AZURE_OPENAI_DEPLOYMENT_NAME
    }
