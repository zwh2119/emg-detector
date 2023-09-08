data_size: int = 4
batch_size: int = 32

label2idx = {
     'forward': 0,
     'left': 1,
     'right': 2,
     # 'grab': 3,

 }

idx2label = dict(zip(label2idx.values(), label2idx.keys()))


