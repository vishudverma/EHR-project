"""
Configuration file for model parameters and constants.
"""

# Model parameters
MODEL_PARAMS = {
    'random_forest': {
        'n_estimators': 100,
        'max_depth': 10,
        'min_samples_split': 2,
        'min_samples_leaf': 1
    },
    'xgboost': {
        'learning_rate': 0.1,
        'max_depth': 6,
        'n_estimators': 100
    },
    'logistic_regression': {
        'C': 1.0,
        'max_iter': 100,
        'solver': 'lbfgs'
    }
}

# Feature engineering parameters
FEATURE_PARAMS = {
    'time_window': 30,  # days
    'categorical_threshold': 10,  # min frequency for categorical values
    'missing_threshold': 0.3  # max missing ratio
}

# Path configurations
DATA_PATHS = {
    'raw_data': '../data/00_raw',
    'interim_data': '../data/01_interim',
    'processed_data': '../data/02_processed',
    'model_output': '../models'
}

# Model evaluation metrics
EVALUATION_METRICS = [
    'accuracy',
    'precision',
    'recall',
    'roc_auc',
    'f1_score'
]
