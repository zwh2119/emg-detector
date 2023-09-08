import time

import requests

url = 'http://192.168.1.1'
port = 2001


def robot_control(data):
    try:
        requests.post(f'{url}:{port}', data=bytes.fromhex(data), timeout=0.5)
    except Exception as e:
        # print(e)
        pass


def grab():
    print('grab')

    # 伸展大臂
    robot_control('FF010437FF')
    sleep()

    # 抓取
    robot_control('FF0102AAFF')
    sleep()


def loosen():
    print('loosen')

    robot_control('FF010288FF')
    sleep()

    robot_control('FF01040FFF')
    sleep()


def forward():
    print('forward')
    robot_control("FF000200FF")


def back():
    print('back')
    robot_control("FF000100FF")


def left():
    print('left')
    robot_control("FF000300FF")
    sleep(0.1)
    stop()


def right():
    print('right')
    robot_control("FF000400FF")
    # robot_control("FF020109FF")
    # robot_control("FF020209FF")

    sleep(0.1)
    stop()


def stop():
    print('stop')
    robot_control('FF000000FF')


def velocity_set():
    robot_control('FF020101FF')
    sleep()
    robot_control('FF020201FF')
    sleep()


def reset():
    print('reset')

    # 行进停止
    stop()
    sleep()

    velocity_set()

    # # 摄像头垂直舵机
    # robot_control('FF010748FF')
    # sleep()
    #
    # # 摄像头水平舵机
    # robot_control('FF010872FF')
    # sleep()

    set_simple_arm()


def special_grab():
    # 机械爪舵机
    robot_control('FF010448FF')
    sleep()

    # 机械大臂舵机
    robot_control('FF01013AFF')
    sleep()


def special_poor():
    # 机械腕舵机
    robot_control('FF010383FF')
    sleep(4)
    robot_control('FF010300FF')


def special_loosen():
    # 机械大臂舵机
    robot_control('FF01011EFF')
    sleep()

    # 机械爪舵机
    robot_control('FF010412FF')
    sleep()

def set_special_arm():
    # 机械爪舵机
    robot_control('FF010412FF')
    sleep()

    # 机械腕舵机
    robot_control('FF010300FF')
    sleep()

    # 机械小臂舵机
    robot_control('FF010279FF')
    sleep()

    # 机械大臂舵机
    robot_control('FF01011EFF')
    sleep()


def set_simple_arm():
    # 机械爪舵机
    robot_control('FF01040FFF')
    sleep()

    # 机械腕舵机
    robot_control('FF01035AFF')
    sleep()

    # 机械小臂舵机
    robot_control('FF010288FF')
    sleep()

    # 机械大臂舵机
    robot_control('FF01012EFF')
    sleep()


# 放置物品
def get_object_1():
    set_simple_arm()
    sleep()
    grab()
    forward()
    sleep(4)
    stop()
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    loosen()
    sleep()
    back()
    sleep(2)
    stop()
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    forward()
    sleep(4)
    stop()
    sleep()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()


# 取水
def get_object_2():
    set_simple_arm()
    sleep()
    forward()
    sleep(4)
    stop()
    sleep()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()
    forward()
    sleep(2)
    stop()
    sleep()
    grab()
    sleep()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()
    forward()
    sleep(4)
    stop()
    sleep()
    loosen()
    sleep()


# 喂猫粮
def get_object_3():
    set_special_arm()
    sleep()
    forward()
    sleep(3)
    stop()
    sleep()
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    forward()
    sleep(1.5)
    stop()
    sleep()
    special_grab()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()
    forward()
    sleep(3)
    stop()
    sleep()
    special_poor()
    sleep()
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    forward()
    sleep(1.5)
    stop()
    sleep()
    special_loosen()
    sleep()
    back()
    sleep(1.5)
    stop()
    left()
    sleep()
    left()
    sleep()
    left()
    sleep()

    back()
    sleep(4.5)
    stop()


def simulate():
    reset()
    sleep(5)
    forward()
    sleep(2)
    stop()
    sleep()
    # left()
    # sleep(2)
    right()
    sleep()
    right()
    sleep()
    right()
    sleep()
    # right()
    # sleep()
    forward()
    sleep(1)
    stop()
    grab()
    sleep()
    left()
    sleep()
    left()
    sleep()
    # left()
    # sleep()
    left()
    sleep()
    forward()
    sleep(1.5)
    stop()
    sleep()
    loosen()



def sleep(second=0.5):
    time.sleep(second)


if __name__ == '__main__':
    reset()
    # left()
    # left()
    # left()
    # right()
    # right()
    # right()
    # reset()
    # left()
    # right()
    # simulate()
    # get_object_1()
    # set_special_arm()
    # special_grab()
    # special_poor()
    # sleep(2)
    # special_loosen()
    # get_object_3()
    get_object_1()