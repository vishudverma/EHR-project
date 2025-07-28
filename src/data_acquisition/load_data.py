import pandas as pd
import os
import requests
from sqlalchemy import create_engine
from config.database_config import DATABASE_URI
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def download_diabetes_data():
    """
    Download the UCI diabetes dataset if it doesn't exist locally.
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00296/dataset_diabetes.zip"
    local_path = os.path.join(RAW_DATA_DIR, "dataset_diabetes.zip")
    csv_path = os.path.join(RAW_DATA_DIR, "diabetes_data.csv")
    
    if not os.path.exists(csv_path):
        print("Downloading diabetes dataset...")
        response = requests.get(url)
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        # Extract the zip file
        import zipfile
        with zipfile.ZipFile(local_path, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_DIR)
        
        # Remove the zip file
        os.remove(local_path)
        print("Dataset downloaded and extracted successfully.")
    
    return csv_path

def load_data(file_path=None):
    """
    Load the raw diabetes dataset.
    """
    if file_path is None:
        file_path = download_diabetes_data()
    
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded data with {len(data)} rows and {len(data.columns)} columns")
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def save_to_database(data, table_name):
    """
    Save the DataFrame to the SQL database.
    """
    try:
        engine = create_engine(DATABASE_URI)
        data.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data saved to table {table_name} in the database.")
        return True
    except Exception as e:
        print(f"Error saving to database: {str(e)}")
        return False

if __name__ == "__main__":
    # Load the data
    diabetes_data = load_data()
    
    if diabetes_data is not None:
        # Save the data to the database
        save_to_database(diabetes_data, 'diabetes_raw')