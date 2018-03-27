import time
from threading import Thread
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def func(name):
    info('function f')
    print("name:" +name)

if __name__ == '__main__':
    info('main line')
    t = Thread(target=func, args=('bob',))
    t = Thread(target=func, args=('allice',))
    t.start()
    t.join()

