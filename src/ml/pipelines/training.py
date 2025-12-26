import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
from src.core.logger import get_logger

logger = get_logger(__name__)

class TrainingPipeline:
    def __init__(self):
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier())
        ])

    def train(self, X, y):
        logger.info("Starting ML training pipeline with GridSearch...")
        param_grid = {
            'classifier__n_estimators': [50, 100],
            'classifier__max_depth': [None, 10]
        }
        
        grid_search = GridSearchCV(self.pipeline, param_grid, cv=5)
        grid_search.fit(X, y)
        
        self.best_model = grid_search.best_estimator_
        logger.info(f"Best parameters: {grid_search.best_params_}")
        return grid_search.best_score_

    def save_model(self, path: str):
        logger.info(f"Saving model to {path}")
        joblib.dump(self.best_model, path)
