#try except finnally
'''
try:
    print("code started")
    raise KeyError
except KeyError as e:
    print("key error")
else:
    print("other error")
finally:
    print("finally")
'''

#with就是为了简化 try finally, 上下文管理器
class Sample():
    def __enter__(self):
        print("enter")
        #获取资源
        return  self
    def __exit__(self, exc_type, exc_val, exc_tb):
        #释放资源
        print("exit")
    def do_somthing(self):
        print("doing something")

with Sample() as sample:
    sample.do_somthing()


#if __name__ == "__main__":
#    result = exe_try()
#    print(result)
