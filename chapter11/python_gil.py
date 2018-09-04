#gil global interpreter lock (cpython)
#python中一个线程对应宇c语言中的一个线程
#gil使得同一个时刻只有一个线程运行在一个cpu上执行字节码,无法将多个线程映射到多个cpu上执行

#import dis
#def add(a):
#    a = a + 1
#    return a

#print(dis.dis(add))
import threading

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#多次运行结果不同,说明并  不是 thread1线程执行完了以后达到1000000，释放掉gil锁，在执行thread2线程 减到0
#而是　会根据执行的字节码行数以及时间片释放gil锁, 还会遇到io的操作时候主动释放

print(total)

