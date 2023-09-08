import sys
from abc import abstractmethod

from config import *


class PredictorBase:
    def __init__(self, model, window_size):
        self.model = model
        self.queue = list()
        self.window_size = window_size

    def predict(self):
        count = 0
        while True:
            count += 1
            x = sys.stdin.readline()
            if count % 10000 == 0:
                sys.stdin.flush()
            # print(x)
            if len(x) == 0:
                break
            try:
                x = [float(i) for i in x.split(',')]
            except ValueError as _:
                continue
                # raise ValueError(f"Please check the input format, making sure it is separated by , in Ascii.")
            if len(x) != data_size:
                # raise RuntimeError(f"Unexpected data input length. Expected:{data_size}, Get:{len(x)}")
                # print(f"Unexpected data input length. Expected:{data_size}, Get:{len(x)}")
                continue

            # if x[0] < 100 or x[1] < 100:
            #     self.queue.clear()
            #     continue

            self.queue.append(x)

            if len(self.queue) < self.window_size:
                continue

            # if len(self.queue) > self.window_size:
            #     self.queue.pop()

            label = self.get_label()
            # if label is not None:
            #     print(label)
            print(label)
            # print(self.get_label())
            for i in range(int(self.window_size//20)):
                self.queue.pop(0)
            # self.queue.pop(0)
            # self.queue.clear()

    @abstractmethod
    def get_label(self):
        pass

    def __call__(self):
        return self.predict()
