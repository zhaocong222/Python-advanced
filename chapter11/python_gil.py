#gil global interpreter lock (cpython)
#python中一个线程对应宇c语言中的一个线程
#gil使得同一个时刻只有一个线程运行在一个cpu上执行字节码,无法将多个线程映射到多个cpu上执行

import dis
def add(a):
    a = a + 1
    return a

print(dis.dis(add))