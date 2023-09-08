import argparser
from models import RNNModel
from config import *
from trainer import Trainer
if __name__ == '__main__':
    parser = argparser.TrainParser()
    args = parser.parse_args()
    model = RNNModel(data_size)
    print(model)
    trainer = Trainer(model, **vars(args))
    trainer()







