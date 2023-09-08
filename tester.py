import logging

import torch
from accelerate import Accelerator
from sklearn import metrics
from torch import nn
from torch.nn import functional
from torch.utils.data import DataLoader
from tqdm import tqdm

from dataset import CustomDataset
from config import *

logger = logging.getLogger("north_star")


class Tester:
    def __init__(
            self,
            model: nn.Module,
            data_file: str,
            in_model_file: str = None,
            window_size:int = 900
    ):
        self.total_steps = None
        self.window_size = window_size

        if in_model_file is not None:
            map_location = torch.device("cpu") if not torch.cuda.is_available() else None
            model.load_state_dict(torch.load(in_model_file, map_location=map_location))
        optimizer = self.create_optimizer(model)

        self.accelerator = Accelerator()
        self.model = model
        # self.model, self.optimizer = self.accelerator.prepare(model, optimizer)
        # self.train_dataloader = self.accelerator.prepare(train_dataloader)
        eval_dataloader = self.get_eval_dataloader(data_file, 32)
        self.eval_dataloader = self.accelerator.prepare(eval_dataloader)

    def test(self):
        with torch.no_grad():

            self.model.eval()
            true_num = 0
            total_num = 0
            for batch_index, [data, gold] in enumerate(self.eval_dataloader):
                predicts = self.model(data).argmax(dim=1).tolist()
                golds = gold.tolist()
                true_num_one = sum([predicts[i] == golds[i] for i in range(len(predicts))])
                total_num_one = len(golds)
                print(f'accuracy:{true_num_one/total_num_one}')
                true_num += true_num_one
                total_num += total_num_one

                # print(metrics.classification_report(golds, predicts))
                # print(metrics.confusion_matrix(golds, predicts))
            print(f'total_acc:{true_num/total_num}')

    @staticmethod
    def create_optimizer(model: nn.Module):
        return torch.optim.AdamW(model.parameters(), lr=3e-4)


    def get_eval_dataloader(self, data_file, batch_size: int):
        eval_dataset = CustomDataset(data_file, window_size=self.window_size)
        return DataLoader(eval_dataset, batch_size=batch_size, shuffle=True)

    def __call__(self):
        return self.test()
