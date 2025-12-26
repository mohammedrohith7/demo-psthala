from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from src.core.logger import get_logger
from src.rag.service import RAGService

logger = get_logger(__name__)

class IngestionPipeline:
    def __init__(self):
        self.rag_service = RAGService()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

    async def ingest_file(self, file_path: str):
        logger.info(f"Starting ingestion for {file_path}")
        
        if file_path.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path)
            
        documents = loader.load()
        chunks = self.text_splitter.split_documents(documents)
        
        logger.info(f"Split document into {len(chunks)} chunks")
        
        # In a real scenario, we would use the self.rag_service.vector_store.add_documents()
        # For now, we simulate the addition
        # await self.rag_service.vector_store.aadd_documents(chunks)
        
        return len(chunks)
