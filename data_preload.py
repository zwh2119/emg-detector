import csv
import os

if __name__ == '__main__':
    cur_dir = os.path.join(os.getcwd(), 'process_data')
    forward_count = 0
    left_count = 0
    right_count = 0
    grab_count = 0
    for file in os.listdir(cur_dir):
        if file.endswith('txt'):
            path = os.path.join(cur_dir, file)
            motion = []
            print(file)
            with open(path, 'r',encoding='utf8') as f:
                for line in f.readlines():
                    if line == '\n':
                        continue
                    # printd(line)
                    dd = line.split(',')
                    motion.append([dd[0], dd[1], dd[3], dd[4]])
            csv_file = file.split('.')[0] + '.csv'
            if 'forward' in csv_file:
                if forward_count < 91:
                    path = 'data/train_data'

                else:
                    path = 'data/test_data'
                forward_count += 1
            if 'left' in csv_file:
                if left_count < 91:
                    path = 'data/train_data'

                else:
                    path = 'data/test_data'
                left_count += 1
            if 'right' in csv_file:
                if right_count < 91:
                    path = 'data/train_data'

                else:
                    path = 'data/test_data'
                right_count += 1
            if 'grab' in csv_file:
                if grab_count < 91:
                    path = 'data/train_data'

                else:
                    path = 'data/test_data'
                grab_count += 1
            with open(os.path.join(os.getcwd(), path, csv_file), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(motion)

            # with open(os.path.join(os.getcwd(), 'data', csv_file), 'w', newline='') as f:
            #     writer = csv.writer(f)
            #     writer.writerows(motion)

