from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.core.config import settings
from src.core.logger import get_logger
from src.app.models import PromptRequest, RAGQueryRequest, MLTrainRequest, EvalRequest

# Service Imports
from src.genai.service import GenAIService
from src.rag.service import RAGService
from src.llm.evaluation import LLMEvaluator

logger = get_logger(__name__)

# Initialize Services
genai_service = GenAIService()
rag_service = RAGService()
evaluator = LLMEvaluator()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} in {settings.ENVIRONMENT} mode")
    yield
    logger.info("Shutting down application...")

app = FastAPI(
    title=settings.APP_NAME,
    version="1.1.0",
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
    return {"message": "Welcome to the Updated Gemini AI MLOps Platform API"}

@app.post("/genai/generate")
async def generate_text(request: PromptRequest):
    logger.info(f"Received generation request")
    try:
        response = await genai_service.generate_response(request.prompt, request.system_message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag/query")
async def rag_query(request: RAGQueryRequest):
    logger.info(f"Received RAG query")
    try:
        result = await rag_service.query(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/llm/evaluate")
async def evaluate_llm(request: EvalRequest):
    logger.info("Received evaluation request")
    result = evaluator.evaluate_response(request.prompt, request.response, request.reference)
    return result

@app.post("/ml/train")
async def train_model(request: MLTrainRequest):
    # This is a placeholder as training usually happens asynchronously
    logger.info(f"Triggering training for {request.data_path}")
    return {"status": "training_initiated", "data": request.data_path}
