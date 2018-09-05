#线程同步 利用锁 -　但是会降低性能
from threading import Lock,RLock #RLock 可重入的锁
import threading

#在同一个线程里面,可以连续调用多次acquire,一定要主要acquire的次数和release次数要相等

total = 0
#lock = Lock()
lock = RLock()

def add():
    global total
    global lock

    for i in range(1000000):
        lock.acquire() #获得锁
        lock.acquire()
        total += 1
        lock.release() #释放锁
        lock.release() #释放锁


def dosomething(lock):
    lock.acquire()
    lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)

#1.用锁会影响性能
#2.锁会引起死锁
