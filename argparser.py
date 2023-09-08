import argparse


class TrainParser(argparse.ArgumentParser):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.add_argument("--data_file", nargs='?', type=str, default='data/train_data')
        self.add_argument('--out_model_file', nargs='?', type=str,
                          default='parameters_100sumdata_900windows_NEWdata_50epoch_10percentage.pt')
        self.add_argument('--in_model_file', nargs='?', type=str,
                          default="parameters_100sumdata_900windows_NEWdata_50epoch_5percentage.pt")
        self.add_argument('--epochs', type=int, default=5)
        self.add_argument('--window_size', type=int, default=900)
        self.add_argument('--debug', action='store_true', default=False)


class TestParser(argparse.ArgumentParser):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.add_argument("--data_file", nargs='?', type=str, default='data/test_data')
        self.add_argument('--in_model_file', nargs='?', type=str,
                          default='parameters_100sumdata_900windows_NEWdata_50epoch_5percentage.pt')
        self.add_argument('--window_size', type=int, default=1000)


class PredictParser(argparse.ArgumentParser):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.add_argument('in_model_file', nargs='?', type=str,
                          default='pretrained_model/parameters_100sumdata_1000windows_olddata_50epoch_25percentage.pt')
        self.add_argument('--window_size', type=int, default=1000)
