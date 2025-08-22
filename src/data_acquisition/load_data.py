import pandas as pd
import os
import requests
import sys
from pathlib import Path
from sqlalchemy import create_engine

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from config.database_config import db_config
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def download_diabetes_data():
    """
    Using multiple sources to create a comprehensive dataset for analysis.
    """
    # Create RAW_DATA_DIR if it doesn't exist
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    url_uci = "https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip"
    url_cms_hgi = "https://data.cms.gov/provider-data/api/1/dataset/27eaefc4-8e32-4ce7-8e05-3cb9a6a34504/download"
    url_cms_rd = "https://data.cms.gov/provider-data/api/1/dataset/2c5a5b2a-5ed3-4c4a-84a6-a2e5b1a8c8a5/download"
    url_cms_hai = "https://data.cms.gov/provider-data/api/1/dataset/4c67c2e9-7e47-4b07-8f37-1a4db5CD50b0/download"

    # Download and process UCI dataset
    local_zip = os.path.join(RAW_DATA_DIR, "dataset_diabetes.zip")
    csv_path = os.path.join(RAW_DATA_DIR, "diabetes_data.csv")
    
    if not os.path.exists(csv_path):
        print("Downloading UCI diabetes dataset...")
        response = requests.get(url_uci)
        with open(local_zip, 'wb') as f:
            f.write(response.content)
        
        # Extract the zip file
        import zipfile
        with zipfile.ZipFile(local_zip, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_DIR)
        
        # Remove the zip file after extraction
        os.remove(local_zip)
        print("UCI dataset downloaded and extracted successfully.")

        # Download CMS datasets
        print("Downloading CMS datasets...")
        cms_urls = {
            "cms_hospital_general_info.csv": url_cms_hgi,
            "cms_readmission_death_measures.csv": url_cms_rd,
            "cms_healthcare_associated_infections.csv": url_cms_hai
        }
        
        for filename, url in cms_urls.items():
            file_path = os.path.join(RAW_DATA_DIR, filename)
            if not os.path.exists(file_path):
                print(f"Downloading {filename}...")
                response = requests.get(url)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"{filename} downloaded successfully.")
    
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
        engine = create_engine(db_config.uri)
        data.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data saved to table {table_name} in the database.")
        return True
    except Exception as e:
        print(f"Error saving to database: {str(e)}")
        return False

def verify_downloads():
    """
    Verify that all required datasets are downloaded and accessible.
    Returns a dictionary with the status of each file.
    """
    expected_files = {
        "diabetes_data.csv": "UCI Diabetes Dataset",
        "cms_hospital_general_info.csv": "CMS Hospital General Information",
        "cms_readmission_death_measures.csv": "CMS Readmission and Death Measures",
        "cms_healthcare_associated_infections.csv": "CMS Healthcare Associated Infections"
    }
    
    verification_results = {}
    for filename, description in expected_files.items():
        file_path = os.path.join(RAW_DATA_DIR, filename)
        try:
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                verification_results[filename] = {
                    "status": "Success",
                    "rows": len(df),
                    "columns": len(df.columns),
                    "size_mb": os.path.getsize(file_path) / (1024 * 1024)
                }
            else:
                verification_results[filename] = {
                    "status": "Missing",
                    "error": f"File not found: {file_path}"
                }
        except Exception as e:
            verification_results[filename] = {
                "status": "Error",
                "error": str(e)
            }
    
    return verification_results

# Update the main block to include verification
if __name__ == "__main__":
    # Load the data
    diabetes_data = load_data()
    
    # Verify all downloads
    verification_results = verify_downloads()
    
    # Print verification results
    print("\nVerification Results:")
    print("-" * 80)
    for filename, result in verification_results.items():
        print(f"\nFile: {filename}")
        if result["status"] == "Success":
            print(f"Status: {result['status']}")
            print(f"Rows: {result['rows']:,}")
            print(f"Columns: {result['columns']}")
            print(f"Size: {result['size_mb']:.2f} MB")
        else:
            print(f"Status: {result['status']}")
            print(f"Error: {result['error']}")
    
    # Only proceed with database save if all files are present
    if all(result["status"] == "Success" for result in verification_results.values()):
        if diabetes_data is not None:
            save_to_database(diabetes_data, 'diabetes_raw')
    else:
        print("\nError: Not all required datasets were downloaded successfully.")