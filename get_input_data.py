import sys
import time

import serial


def get_input_data(buffer: list = None):
    ser = serial.Serial('COM7', 115200, timeout=1)
    string_queue = ''
    for i in range(100):
        a = ser.read()

    while True:
        a = ser.read()
        try:
            s = a.decode()
        except:
            string_queue = ''
            continue

        if s == ',' or s.isdigit():
            string_queue += s
        elif s == '\r':
            try:
                actions = string_queue.split(',')
                if len(actions) != 7:
                    string_queue = ''
                    continue
                actions_try = [int(x) for x in actions[:-1]]
                if actions[0].isdigit() and actions[1].isdigit() and actions[3].isdigit() and actions[4].isdigit():
                    put_string = ','.join([actions[0], actions[1], actions[3], actions[4]])
                    print(put_string)
                    # buffer.append(put_string)
                string_queue = ''
            except:
                string_queue = ''
                continue

        elif s == '\n':
            try:
                actions = string_queue.split(',')
                if len(actions) != 7:
                    string_queue = ''
                    continue
                actions_try = [int(x) for x in actions[:-1]]
                put_string = ','.join(actions[:-1])
                print(put_string)
                # buffer.append(put_string)
                string_queue = ''
            except:
                string_queue = ''
                continue
        else:
            string_queue = ''
            continue


if __name__ == '__main__':
    get_input_data()
