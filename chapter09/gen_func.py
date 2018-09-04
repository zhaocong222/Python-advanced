#生成器函数,函数里只要有yield关键字
def gen_func():
    yield 1

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n < index:
        re_list.append(b)
        a,b = b,a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a,b = b,a+b
        n += 1

for data in gen_fib(10):
    print(data)

if __name__ == "__main__":
    #生成器对象
    gen = gen_func()
    #print(next(gen))

