from multiprocessing import Process
import time

sec = 0
max_time = 5 # sec

def func1():
    global sec
    print ('start func1')
    while sec < max_time:
        sec += 1
        time.sleep(1)
    print ('end func1')

def func2():
    global sec
    print ('start func2')
    while sec < max_time:
        sec += 1
        time.sleep(1)
    print ('end func2')

if __name__=='__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    input()
