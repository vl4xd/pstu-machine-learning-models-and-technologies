import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


class Model1():
    def __init__(self):
        self.scaler: StandardScaler = self.__get_scaler()
        self.model: LinearRegression = self.__get_model()

    def __get_scaler(self, path: str = './pipeline/scaler_1.pickle') -> StandardScaler:
        with open(path, 'rb') as file:
            return pickle.load(file)

    def __get_model(self, path: str = './pipeline/lr_model_1.pickle') -> LinearRegression:
        with open(path, 'rb') as file:
            return pickle.load(file)

    def predict(self, humidity: float, temperature: float) -> float:
        pass