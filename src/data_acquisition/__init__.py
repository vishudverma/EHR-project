"""
Data Acquisition Package

A modular pipeline for acquiring, verifying, and storing raw EHR and CMS data for the readmission risk model.
Designed for reproducibility and ease of use.
"""

from .01_data_acquisition import  download_kaggle_datasets,download_web_datasets # type: ignore
from .data_verification import validate_schema, check_data_quality, generate_verification_report # type: ignore
from .data_upload import save_to_raw_folder, create_mssql_connection, upload_dataframe_to_mssql, update_data_manifest # type: ignore

# This allows us to write:
# from src.data_acquisition import download_uci_diabetes_dataset, validate_schema
# making the code cleaner.