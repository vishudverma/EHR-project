import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project base paths
PROJECT_ROOT = Path(__file__).parent.parent  # This will now point to EHR-project
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Database configurations
DB_CONFIG = {
    "server": os.getenv("DB_SERVER", "localhost"),
    "database": os.getenv("DB_NAME", "ehr_readmission"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "driver": os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
}

# Add DATABASE_URI
DATABASE_URI = f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver'].replace(' ', '+')}"

# Data processing configurations
MISSING_THRESHOLD = 0.4  # Remove features with >40% missing values
RANDOM_STATE = 42

# Table names
RAW_DATA_TABLE = "diabetes_raw"
PROCESSED_DATA_TABLE = "diabetes_processed"

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR]:
    os.makedirs(directory, exist_ok=True)