#__getattr__, __getattribute
#__getattr__ 就是在查找不到属性的时候调用
from datetime import date,datetime
import numbers

#属性描述符
class InField:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int value need")
        self.value = value
    def __delete__(self, instance):
        pass

class User:
    age = InField()


'''
class User:
    def __init__(self,name,birthday,info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    #查找不到会进入
    def __getattr__(self, item):
        return self.info[item]

    #只要使用 user.属性　就会进入这个方法，对比与上面区别,不推荐使用
    #def __getattribute__(self, item):
    #    return "boddy"
'''



if __name__ == "__main__":
    #user = User("bobby", date(year=1987, month=1, day=1),info={"company_name":"immoc"})
    #print(user.company_name)
    user = User()
    user.age = 10
    print(user.age)
    #ValueError: int value need
    #user.age = 'aaa'
