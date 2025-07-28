import os
import pyodbc
from typing import Dict, Optional

# Import configurations from __init__.py
from . import DB_CONFIG, DATABASE_URI

class DatabaseConfig:
    def __init__(self, config: Dict = DB_CONFIG):
        self.config = config
        self.database_uri = DATABASE_URI
        self.validate_config()

    def validate_config(self) -> None:
        """Validate required configuration parameters."""
        required_params = ['server', 'database', 'username', 'password', 'driver']
        missing_params = [param for param in required_params if not self.config.get(param)]
        if missing_params:
            raise ValueError(f"Missing required database parameters: {', '.join(missing_params)}")

    def get_pyodbc_connection_string(self) -> str:
        """Generate connection string for pyodbc."""
        return (f"DRIVER={{{self.config['driver']}}};"
                f"SERVER={self.config['server']};"
                f"DATABASE={self.config['database']};"
                f"UID={self.config['username']};"
                f"PWD={self.config['password']}")

    def get_sqlalchemy_connection_string(self) -> str:
        """Generate connection string for SQLAlchemy."""
        return (f"mssql+pyodbc://{self.config['username']}:"
                f"{self.config['password']}@{self.config['server']}/"
                f"{self.config['database']}?driver={self.config['driver'].replace(' ', '+')}")

    def get_connection(self) -> Optional[pyodbc.Connection]:
        """Create and return a database connection."""
        try:
            return pyodbc.connect(self.get_pyodbc_connection_string())
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None

    @property
    def uri(self) -> str:
        """Return the database URI."""
        return self.database_uri

# Create default instance
db_config = DatabaseConfig()