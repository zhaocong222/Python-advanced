class A:
    name = "A"
    def __init__(self):
        self.name = "obj"

a = A()
print(a.name)

class d:
    pass

class c(d):
    pass

class b(d):
    pass

class a(b,c):
    pass

print(a.__mro__)