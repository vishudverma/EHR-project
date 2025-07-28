import pandas as pd
import os
import sqlalchemy
from sqlalchemy import create_engine
from config.database_config import DATABASE_URI

def load_data(file_path):
    """
    Load the raw diabetes dataset from the specified file path.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    data = pd.read_csv(file_path)
    return data

def save_to_database(data, table_name):
    """
    Save the DataFrame to the SQL database.
    """
    engine = create_engine(DATABASE_URI)
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data saved to table {table_name} in the database.")

if __name__ == "__main__":
    # Load the data
    raw_data_path = os.path.join('data', 'raw', 'diabetes_data.csv')
    diabetes_data = load_data(raw_data_path)
    
    # Save the data to the database
    save_to_database(diabetes_data, 'diabetes_data')