#我们检查某个类是否有某种方法
class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby","bobby2"])
print(len(com))

print(hasattr(com,"__len__"))

from collections.abc import Sized
isinstance(com,Sized)

