import time

import serial
import chardet
import winsound
import threading



# ser = serial.Serial('COM5', 115200, timeout=1)
# #
# print(ser.isOpen())
#
# skip = True
# for i in range(50000000):
#     a = ser.read()
#     if i < 20:
#         continue
#     if a == b'\n':
#         skip = False
#     if skip:
#         continue
#
# # # a.decode(encoding='utf-8')
#     try:
#         a.decode()
#         print(a.decode(), end='')
#     except:
#         continue
#
# ser.close()
# ser.open()

# print(ser.isOpen())

# a = []
# for i in range(1000):
#     a.append(ser.read())

    # print(int(aa, base=2))
    # a += aa
# print(ser.read())
# for i in range(5):
#     print(ser.read(), end=' ')
# print(ser.readall())

# print(a)
# for i in a:
#     print(int.from_bytes(i, 'big'))
# ser.close()


def beep_function():
    time.sleep(5)
    winsound.Beep(1000, 100)
    time.sleep(3)
    winsound.Beep(1000, 100)
if __name__ == '__main__':
    t = threading.Thread(target=beep_function)
    ser = serial.Serial('COM3', 115200, timeout=1)
    record = False
    skip = True
    file = "use_data/grab60.txt"
    motion = []
    start = time.time()
    t.start()
    for i in range(500000000):
        a = ser.read()
        # if i < 20:
        #     continue
        if not record and time.time() - start > 5:

            record = True
        if record and time.time() - start > 8:

            record = False
            break

        if record:
            if a == b'\n':
                skip = False
            if skip:
                continue
            motion.append(a.decode())

    with open(file, 'w') as f:
        for m in motion:
            f.write(m)




