from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class BaseResponse(BaseModel):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = {}

class AIResponse(BaseResponse):
    content: str
    usage: Optional[Dict[str, int]] = None

class RAGResponse(AIResponse):
    source_documents: List[Dict[str, Any]] = []

class EvaluationMetrics(BaseModel):
    relevance: float
    faithfulness: float
    answer_relevance: float
    context_precision: Optional[float] = None
