from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class PromptRequest(BaseModel):
    prompt: str
    system_message: Optional[str] = "You are a helpful assistant."

class RAGQueryRequest(BaseModel):
    query: str

class MLTrainRequest(BaseModel):
    data_path: str
    target_column: str

class EvalRequest(BaseModel):
    prompt: str
    response: str
    reference: Optional[str] = None
