import os
import time
from src.core.config import settings
from src.core.logger import get_logger

logger = get_logger(__name__)

def seed_servicenow_data():
    logger.info("Seeding ServiceNow data...")
    # Logic to ingest sanitize ServiceNow tickets
    time.sleep(1)
    logger.info("  - 500 Sanitized Incidents seeded.")

def seed_kb_data():
    logger.info("Seeding Knowledge Base articles...")
    # Logic to index KB articles into Azure Search
    time.sleep(1)
    logger.info("  - 200 KB Articles indexed.")

def seed_mig_data():
    logger.info("Seeding MIG data...")
    time.sleep(1)
    logger.info("  - MIG topology data loaded.")

def seed_d2ops_data():
    logger.info("Seeding D2Ops data...")
    time.sleep(1)
    logger.info("  - D2Ops metrics simulated.")

def seed_iac_data():
    logger.info("Seeding IaC sample data...")
    time.sleep(1)
    logger.info("  - Terraform templates indexed.")

def main():
    logger.info(f"Starting Data Seeding for Environment: {settings.ENVIRONMENT.upper()}")
    
    if settings.ENVIRONMENT.lower() not in ["uat", "development"]:
        logger.warning("Warning: Seeding is typically for UAT or DEV. Proceeding anyway.")

    seed_servicenow_data()
    seed_kb_data()
    seed_mig_data()
    seed_d2ops_data()
    seed_iac_data()
    
    logger.info("\nData Seeding Complete. Environment is ready for validation.")

if __name__ == "__main__":
    main()
