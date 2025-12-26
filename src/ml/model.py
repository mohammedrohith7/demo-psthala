import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.core.logger import get_logger

logger = get_logger(__name__)

class MLModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data: pd.DataFrame, target_col: str):
        logger.info("Training classical ML model...")
        X = data.drop(columns=[target_col])
        y = data[target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        logger.info(f"Model trained with accuracy: {score}")
        return score

    def predict(self, X: pd.DataFrame):
        return self.model.predict(X)
