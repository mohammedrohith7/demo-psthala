from src.core.logger import get_logger

logger = get_logger(__name__)

def preprocess_text(text: str):
    """
    Standard text preprocessing for AI tasks.
    """
    logger.debug("Preprocessing text")
    return text.strip().lower()

def format_prompt(template: str, **kwargs):
    """
    Helper to format prompts.
    """
    return template.format(**kwargs)
