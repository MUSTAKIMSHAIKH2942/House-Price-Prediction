# models/xgboost_model.py
from xgboost import XGBRegressor
import joblib
from models.base_model import BaseModel

class XGBoostModel(BaseModel):
    def __init__(self):
        self.model = XGBRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, filename):
        joblib.dump(self.model, filename)

    def load(self, filename):
        self.model = joblib.load(filename)
