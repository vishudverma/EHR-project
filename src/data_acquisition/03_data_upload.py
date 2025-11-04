import os
import sqlalchemy # type:ignore
import pandas as pd # type:ignore
import pyodbc # type:ignore

# Using the server name available on the system and using the windows authentication options
SERVER = 'VISHUD_LAPTOP\\SQLEXPRESS' # Change the `SERVER` and `DATABASE` name as suited for your project 
DATABASE = 'ehr_readmission'
DRIVER = 'ODBC Driver 17 for SQL Server'

# Creating the engine to connect
engine = sqlalchemy.create_engine(f"mssql+pyodbc:///?odbc_connection=DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;")

# The data thats inputed here is primarily cleaned using the /notebooks/01_eda_initial.ipynb
# Create the data files for the import 
raw_data_folder = os.path.abspath('data/01_interim')
file_list = os.listdir(raw_data_folder)

for file in file_list:
    file_path = os.path.join(raw_data_folder, file)
    if file.lower().endswith('.csv'):
        file_path = os.path.join(raw_data_folder,file)
        df = pd.read_csv(file_path)
        try:
            df.to_sql(
                name=f"raw_{os.path.splitext(file)[0]}",
                con=engine,
                if_exists='replace',
                index=False
            )
            print(f"Data form the {file} has been uploaded succesfully.")
        except Exception as e:
            print(f"An error {e} occured while uploading the {file}.")
    elif file.lower().endswith('.xpt'):
        file_path = os.path.join(raw_data_folder, file)
        try:
            df = pd.read_sas(file_path)
            table_name = f"raw_{os.path.splitext(file)[0]}"  # Remove file extension from table name
            # ToDo: make the data have csv extensions and not other formats cause pyodbc cannot handle other formats.
            df.to_sql(
                name=table_name,
                con=engine,
                if_exists='replace',
                index=False,
                schema='dbo'  # Explicitly specify the schema
            )
            print(f"Data form the {file} has been uploaded succesfully.")
        except Exception as e:
            print(f"An error {e} occured while uploading the {file}.")