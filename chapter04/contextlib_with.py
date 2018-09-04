import contextlib

#用装饰器变成上下管理器 , 利用生成器
@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("bobby.txt") as f_opened:
    print("file processing")