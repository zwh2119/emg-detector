import logging

import torch
from accelerate import Accelerator
from sklearn import metrics
from torch import nn
from torch.nn import functional
from torch.utils.data import DataLoader
from tqdm import tqdm

import numpy as np

from dataset import CustomDataset
from config import *

logger = logging.getLogger("north_star")


class Trainer:
    def __init__(
            self,
            model: nn.Module,
            epochs: int,
            data_file: str,
            out_model_file: str,
            in_model_file: str = None,
            debug: bool = False,
            window_size = 800,
            device: str = 'cpu'
    ):
        self.total_steps = None

        self.epochs: int = epochs
        self.window_size = window_size
        self.out_model_file: str = out_model_file
        self.tmp_out_model_file: str = 'tmp_' + out_model_file
        self.device = torch.device(device)

        if in_model_file is not None:
            map_location = torch.device("cpu") if not torch.cuda.is_available() else None
            model.load_state_dict(torch.load(in_model_file, map_location=map_location))
        optimizer = self.create_optimizer(model)

        train_dataloader = self.get_train_dataloader(data_file, batch_size)

        self.accelerator = Accelerator()
        self.model, self.optimizer = self.accelerator.prepare(model, optimizer)
        self.model = self.model.to(self.device)
        self.train_dataloader = self.accelerator.prepare(train_dataloader)

        if debug:
            eval_dataloader = self.get_eval_dataloader(32)
            self.eval_dataloader = self.accelerator.prepare(eval_dataloader)

        self.debug = debug

    def train(self):

        for epoch_index in range(self.epochs):
            with tqdm(total=len(self.train_dataloader), desc=f"Epoch {epoch_index}") as tbar:
                self.model.train()
                loss_list = []
                for batch_index, [data, gold] in enumerate(self.train_dataloader):
                    self.optimizer.zero_grad()
                    data = data.to(self.device)
                    gold = gold.to(self.device)
                    prediction = self.model(data)
                    # print(prediction)
                    # print(gold)
                    loss = functional.cross_entropy(prediction, gold, label_smoothing=0.5)

                    loss = loss.to(self.device)
                    # print(loss)3
                    self.accelerator.backward(loss)
                    self.optimizer.step()
                    loss_list.append(loss.item())
                    tbar.set_postfix(loss=loss.item())
                    tbar.update()
                print(f'Epoch:{epoch_index}     average loss: {np.asarray(loss_list).mean()}')

            if self.debug:
                with torch.no_grad():
                    self.model.eval()
                    predicts, golds = [], []
                    for batch_index, [data, gold] in enumerate(self.eval_dataloader):
                        predicts += self.model(data).argmax(dim=1).tolist()
                        golds += gold.tolist()

                    logger.info("\n" + metrics.classification_report(golds, predicts))
                    logger.info("\n" + str(metrics.confusion_matrix(golds, predicts)))

            torch.save(self.model.state_dict(), self.tmp_out_model_file)

        torch.save(self.model.state_dict(), self.out_model_file)

    @staticmethod
    def create_optimizer(model: nn.Module):
        return torch.optim.AdamW(model.parameters(), lr=3e-4)

    def get_train_dataloader(self, data_file: str, batch_size: int):
        train_dataset = CustomDataset(data_file, window_size=self.window_size)
        self.total_steps = (len(train_dataset) // batch_size + 1) * self.epochs
        return DataLoader(train_dataset, batch_size=batch_size, shuffle=True)


    def get_eval_dataloader(self, batch_size: int):
        eval_dataset = CustomDataset('data/test_data', window_size=self.window_size)
        return DataLoader(eval_dataset, batch_size=batch_size, shuffle=True)

    def __call__(self):
        return self.train()


