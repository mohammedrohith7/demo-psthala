from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.core.config import settings
from src.core.logger import get_logger
from src.core.monitoring import setup_tracing, tracer
from src.app.models import PromptRequest, RAGQueryRequest, MLTrainRequest, EvalRequest

# Service Imports
from src.genai.service import GenAIService
from src.genai.prompts.manager import PromptManager
from src.rag.service import RAGService
from src.rag.ingestion.pipeline import IngestionPipeline
from src.llm.evaluation import LLMEvaluator

logger = get_logger(__name__)

# Initialize Services
setup_tracing()
genai_service = GenAIService()
rag_service = RAGService()
ingestion_pipeline = IngestionPipeline()
evaluator = LLMEvaluator()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting complex {settings.APP_NAME} in {settings.ENVIRONMENT} mode")
    yield
    logger.info("Shutting down application...")

app = FastAPI(
    title=settings.APP_NAME,
    version="2.0.0",
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
    with tracer.start_as_current_span("health_check"):
        logger.debug("Health check requested")
        return {
            "status": "healthy",
            "app_name": settings.APP_NAME,
            "environment": settings.ENVIRONMENT
        }

@app.get("/")
async def root():
    return {"message": "Welcome to the Complex Gemini AI MLOps Platform v2.0"}

@app.post("/genai/generate")
async def generate_text(request: PromptRequest):
    with tracer.start_as_current_span("genai_generate"):
        logger.info(f"Received generation request")
        try:
            # Enhanced with PromptManager
            prompt = PromptManager.get_prompt("basic_chat", query=request.prompt)
            response = await genai_service.generate_response(prompt, request.system_message)
            return {"response": response}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/genai/prompts")
async def list_prompts():
    return {"templates": PromptManager.list_templates()}

@app.post("/rag/query")
async def rag_query(request: RAGQueryRequest):
    with tracer.start_as_current_span("rag_query"):
        logger.info(f"Received RAG query")
        try:
            result = await rag_service.query(request.query)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag/ingest")
async def ingest_document(file_path: str, background_tasks: BackgroundTasks):
    logger.info(f"Ingestion requested for {file_path}")
    background_tasks.add_task(ingestion_pipeline.ingest_file, file_path)
    return {"status": "ingestion_started", "file": file_path}

@app.post("/llm/evaluate")
async def evaluate_llm(request: EvalRequest):
    logger.info("Received evaluation request")
    result = evaluator.evaluate_response(request.prompt, request.response, request.reference)
    return result

@app.post("/ml/train")
async def train_model(request: MLTrainRequest):
    logger.info(f"Triggering training for {request.data_path}")
    # Integration with complex TrainingPipeline would go here
    return {"status": "training_initiated", "data": request.data_path}
