import time
from threading import Thread
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def func(name):
    print("name:" +name)
    info('function f')

if __name__ == '__main__':
    info('main line')
    t = Thread(target=func, args=('bob',))
    t2 = Thread(target=func, args=('allice',))
    t.start()
    t2.start()
    t2.join()
    t.join()

