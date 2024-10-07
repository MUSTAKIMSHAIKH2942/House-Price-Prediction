# models/random_forest_model.py
from sklearn.ensemble import RandomForestRegressor
import joblib
from models.base_model import BaseModel

class RandomForestModel(BaseModel):
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, filename):
        joblib.dump(self.model, filename)

    def load(self, filename):
        self.model = joblib.load(filename)
