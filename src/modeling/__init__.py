# src/modeling/__init__.py
from .01_train_baseline import train_logistic_regression # type: ignore
from .02_train_advanced import train_xgboost_model, optimize_hyperparameters # type: ignore
from .03_evaluate_model import evaluate_model, plot_roc_curve, plot_feature_importance # type: ignore

# Now we can import directly:
# from src.modeling import train_logistic_regression, evaluate_model