# model_factory.py
from models.linear_model import LinearModel
from models.random_forest_model import RandomForestModel
from models.xgboost_model import XGBoostModel

class ModelFactory:
    @staticmethod
    def create_model(model_type):
        if model_type == 'linear':
            return LinearModel()
        elif model_type == 'random_forest':
            return RandomForestModel()
        elif model_type == 'xgboost':
            return XGBoostModel()
        else:
            raise ValueError("Invalid model type")
