import torch
from torch import nn
from PredictBase import PredictorBase
from config import *


class Predictor(PredictorBase):
    def __init__(self, model: nn.Module, in_model_file: str, window_size):
        super().__init__(model, window_size)
        self.model.load_state_dict(torch.load(in_model_file))

    def get_label(self):
        if not self.judge_fierce():
            return 'none'
        sample = torch.tensor(self.queue)
        # print(2)
        # print(self.model(sample.unsqueeze(0)))
        res = self.model(sample.unsqueeze(0))
        # print(3)
        # print(res)
        # if res[0][res.argmax().item()].item() < 1.2:
        #     print(res[0][res.argmax().item()].item(), '  not  ', idx2label[res.argmax().item()])
        #     return None
        # else:
        #     print(res[0][res.argmax().item()].item(), '  is  ', idx2label[res.argmax().item()])
        #     return idx2label[res.argmax().item()]
        return idx2label[res.argmax().item()]

    def judge_fierce(self):
        count = []
        boundry = 100
        for x in self.queue:
            # print('x')
            if x[0] > boundry and x[1] > boundry:
                count.append(1)
            else:
                count.append(0)
        if sum(count) > len(self.queue) * 0.6 and sum(count[len(count) * 2 // 3:]) > len(self.queue) * (1 / 3) * 0.7:
            return True
        else:
            return False
