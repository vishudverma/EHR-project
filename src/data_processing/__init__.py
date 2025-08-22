# src/data_processing/__init__.py
from .01_data_cleaning import load_raw_data, clean_demographics, handle_missing_values # type: ignore
from .02_feature_engineering import calculate_readmission_target, create_temporal_features, engineer_clnical_flags # type: ignore
from .03_data_validation import validate_dataset_schema # type: ignore

# This allows us to write:
# from src.data_processing import load_raw_data, calculate_readmission_target
# instead of more cumbersome:
# from src.data_processing.01_data_cleaning import load_raw_data