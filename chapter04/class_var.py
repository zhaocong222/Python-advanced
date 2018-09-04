class A:
    aa = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y

#先查找a实例本身self -> a
#如果没查到实例a属性 再向上查找 类A的属性
#aa是类属性   x,y是实例属性

a = A(2,3)
A.aa = 11
a.aa = 100
print(a.x ,a.y,a.aa)
print(A.aa)