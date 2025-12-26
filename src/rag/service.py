from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_community.vectorstores.azuresearch import AzureSearch
from src.core.config import settings
from src.core.logger import get_logger

logger = get_logger(__name__)

class RAGService:
    def __init__(self):
        self.embeddings = AzureOpenAIEmbeddings(
            azure_deployment=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
            openai_api_version=settings.AZURE_OPENAI_API_VERSION,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
        )
        
        self.vector_store = AzureSearch(
            azure_search_endpoint=settings.AZURE_SEARCH_ENDPOINT,
            azure_search_key=settings.AZURE_SEARCH_KEY,
            index_name=settings.AZURE_SEARCH_INDEX_NAME,
            embedding_function=self.embeddings.embed_query,
        )
        
        self.llm = AzureChatOpenAI(
            azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            openai_api_version=settings.AZURE_OPENAI_API_VERSION,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
        )

    async def query(self, user_query: str):
        try:
            # Perform similarity search
            docs = self.vector_store.similarity_search(user_query, k=3)
            context = "\n".join([doc.page_content for doc in docs])
            
            # Simple RAG prompt
            prompt = f"""Use the following context to answer the user's question. If you don't know the answer, say you don't know.
            
            Context:
            {context}
            
            Question: {user_query}
            
            Answer:"""
            
            response = self.llm.invoke(prompt)
            return {
                "answer": response.content,
                "sources": [doc.metadata for doc in docs]
            }
        except Exception as e:
            logger.error(f"Error in RAG query: {str(e)}")
            raise e
