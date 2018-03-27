from multiprocessing import Process
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
    p = Process(target=func, args=('bob',))
    p2 = Process(target=func, args=('allice',))
    p.start()
    p2.start()
    p2.join()
    p.join()

