from loguru import logger
from app.config import settings

def setup_logging():
    logger.add("logs/api.log", rotation="10 MB", retention="10 days", level=settings.log_level)
    logger.info("Logging initialized")

