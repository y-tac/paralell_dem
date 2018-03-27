import time
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def func(name):
    info('function f')
    print("name:" +name)
    time.sleep(400)

if __name__ == '__main__':
    info('main line')
    p = Process(target=func, args=('bob',))
    p = Process(target=func, args=('allice',))
    p.start()
    p.join()

