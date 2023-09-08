import time

import serial
import chardet
import winsound
import threading


def read_and_motion():
    ser = serial.Serial('COM7', 115200, timeout=1)
    record = False
    skip = True
    motion = []

    while True:
        a = ser.read()
        print(a)


if __name__ == '__main__':
    read_and_motion()
