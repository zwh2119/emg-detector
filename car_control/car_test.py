import time
import serial


def forward(s: serial.Serial, second):
    print('forward')
    data = bytes.fromhex("FF000200FF")
    ser.write(data)

    time.sleep(second)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)

    time.sleep(1)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)


def right(s: serial.Serial):
    print('right')
    data = bytes.fromhex("FF000400FF")
    ser.write(data)

    time.sleep(1)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)

    time.sleep(1)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)


def left(s: serial.Serial):
    print('left')
    data = bytes.fromhex("FF000300FF")
    ser.write(data)

    time.sleep(1)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)

    time.sleep(1)
    data = bytes.fromhex('FF000000FF')
    ser.write(data)


def grab(s: serial.Serial):
    print('grab')

    time.sleep(1)

    data = bytes.fromhex('FF010437FF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF0102AAFF')
    ser.write(data)



def loosen(s: serial.Serial):
    print('loosen')

    time.sleep(1)

    data = bytes.fromhex('FF010288FF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF01040FFF')
    ser.write(data)


def reset(s: serial.Serial):
    print('reset')
    data = bytes.fromhex('FF000000FF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF01075AFF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF010800FF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF01040FFF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF01035AFF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF010288FF')
    ser.write(data)

    time.sleep(1)

    data = bytes.fromhex('FF01012EFF')
    ser.write(data)


if __name__ == '__main__':
    ser = serial.Serial('COM7', 9600, timeout=5)

    data = bytes.fromhex("FF010320FF")
    ser.write(data)
    time.sleep(65)
    print('start')

    reset(ser)

    time.sleep(4)

    right(ser)
    time.sleep(4)

    right(ser)

    time.sleep(4)

    right(ser)

    time.sleep(4)

    forward(ser, 4)

    time.sleep(4)

    grab(ser)

    time.sleep(4)

    left(ser)

    time.sleep(4)

    left(ser)

    time.sleep(4)

    left(ser)

    time.sleep(4)

    forward(ser, 2)

    time.sleep(4)

    loosen(ser)

    time.sleep(4)
