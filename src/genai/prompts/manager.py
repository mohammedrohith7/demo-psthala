from typing import Dict, Any
from src.core.logger import get_logger

logger = get_logger(__name__)

class PromptManager:
    _templates = {
        "basic_chat": "You are a helpful assistant. User query: {query}",
        "rag_expert": "Use the following context to answer the user question. \nContext: {context} \nQuestion: {query}",
        "code_reviewer": "You are a senior developer. Review the following code for bugs and performance issues: \n{code}"
    }

    @classmethod
    def get_prompt(cls, template_name: str, **kwargs) -> str:
        template = cls._templates.get(template_name)
        if not template:
            logger.error(f"Template {template_name} not found")
            raise ValueError(f"Template {template_name} not found")
        
        try:
            return template.format(**kwargs)
        except KeyError as e:
            logger.error(f"Missing variable for template {template_name}: {str(e)}")
            raise

    @classmethod
    def list_templates(cls):
        return list(cls._templates.keys())
