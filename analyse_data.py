import matplotlib.pyplot as plt


def preprocess_data(file):
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    with open(file, 'r') as f:
        # print(f.readlines())
        for line in f.readlines():
            if line == '\n':
                continue
            print(line)
            data = line.split(',')
            d1.append(int(data[0]))
            d2.append(int(data[1]))
            d3.append(int(data[3]))
            d4.append(int(data[4]))
    return d1, d2, d3, d4

def plot_pic(motion):
    left_down, left_up, right_down, right_up = preprocess_data(f'{motion}.txt')
    assert len(left_down) == len(left_up) == len(right_down) == len(right_up)
    length = len(left_down)
    x = list(range(length))
    plt.plot(x, left_down, color='blue', label='left down left')
    plt.plot(x, left_up, color='red', label="left down right")
    plt.plot(x, right_down, color='orange', label='left up left')
    plt.plot(x, right_up, color='green', label='left up right')
    plt.legend()
    plt.savefig(f'{motion}.png')
    plt.show()


if __name__ == '__main__':
   plot_pic("grab60")
   #   plot_pic('left2"09')
   #  plot_pic('left270')
   #  preprocess_data('forward257.txt')
