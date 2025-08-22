import os
import pyodbc
from typing import Dict, Optional

# Import configurations from __init__.py
from . import DB_CONFIG

class DatabaseConfig:
    def __init__(self, config: Dict = DB_CONFIG):
        self.config = config
        self.validate_config()

    def validate_config(self) -> None:
        """Validate required configuration parameters."""
        required_params = ['server', 'database', 'driver']  # Removed username and password requirement
        missing_params = [param for param in required_params if not self.config.get(param)]
        if missing_params:
            raise ValueError(f"Missing required database parameters: {', '.join(missing_params)}")

    def get_pyodbc_connection_string(self) -> str:
        """Generate connection string for pyodbc using Windows Authentication."""
        return (f"DRIVER={{{self.config['driver']}}};"
                f"SERVER={self.config['server']};"
                f"DATABASE={self.config['database']};"
                "Trusted_Connection=yes;")  # This enables Windows Authentication

    def get_sqlalchemy_connection_string(self) -> str:
        """Generate connection string for SQLAlchemy using Windows Authentication."""
        return (f"mssql+pyodbc://{self.config['server']}/{self.config['database']}?"
                f"driver={self.config['driver'].replace(' ', '+')};"
                "Trusted_Connection=yes")

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
        return self.get_sqlalchemy_connection_string()

# Create default instance
db_config = DatabaseConfig()