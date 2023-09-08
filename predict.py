from argparser import PredictParser
from config import *
from models import RNNModel
from predictor import Predictor


def predict():
    parser = PredictParser()
    model = RNNModel(data_size)
    predictor = Predictor(model, **vars(parser.parse_args()))
    predictor()


if __name__ == "__main__":
    predict()
