import subprocess

if __name__ == '__main__':
    proc_data = subprocess.Popen(
        "D:\\Python\\Anaconda\\envs\\Torch\\python.exe get_input_data.py",
        cwd='.',
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE
    )
    proc_algo = subprocess.Popen(
        "D:\\Python\\Anaconda\\envs\\Torch\\python.exe predict.py",
        cwd='.',
        stdin=proc_data.stdout,
        stdout=subprocess.PIPE,

    )
    assert proc_algo.stdout

    try:
        assert proc_algo.stderr
        for line in proc_algo.stderr:
            print(line.decode())
    except Exception as e:
        print(e)

    for line in proc_algo.stdout:
        print(line.decode())

    while proc_data.poll() is None or proc_algo.poll() is None:
        # for line in proc_algo.stdout:
        #     # print(':')
        #     print(line.decode())
        continue

