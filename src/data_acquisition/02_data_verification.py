import os
import zipfile
import pandas as pd #type:ignore

#TODO: add the rest of the functions to check whether the downloaded data is of the required quality and schema, verify the completeness, and generate a report.

data_path = os.path.abspath('data/00_raw') # This points to the raw data directory

zip_file_path = os.path.join(data_path, 'diabetes+130-us+hospitals+for+years+1999-2008.zip')

def validate_schema():
    # Unzip the file if it exists
    if os.path.exists(zip_file_path) and os.path.exists(os.path.join(data_path, 'diabetic_data.csv'))==False:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(data_path)
        print(f"Extracted {zip_file_path} to {data_path}")
    else:
        print(f"File is already extracted or it does not exist.")

    # Example: Load datasets to verify they are correctly downloaded
    # Adjust file names as per actual downloaded files
    cdc_dataset = pd.read_sas(os.path.join(data_path, 'DEMO_L.xpt'))
    diabetes_pima_dataset = pd.read_csv(os.path.join(data_path, 'diabetes.csv'))
    india_hospital_admissions_dataset = pd.read_csv(os.path.join(data_path, 'HDHI Admission data.csv'))


print(f"Data path is set to: {data_path}, checking if the datasets are accessible\n If the program throws no error it is successful\n If it throws an error please check the /src/data_acquisition/01_data_acquisition.py file for the download functions and ensure the datasets are downloaded correctly.")
validate_schema()

# This verifies that all the datasets are loaded correctly and can be read using the required libraries.