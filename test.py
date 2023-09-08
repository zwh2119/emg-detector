import argparser
from models import RNNModel
from config import *
from tester import Tester


if __name__ == '__main__':
    parser = argparser.TestParser()
    model = RNNModel(data_size)
    tester = Tester(model, **vars(parser.parse_args()))
    tester()

