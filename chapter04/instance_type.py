class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b,B))
print(isinstance(b,A))

#尽量使用type
#print(type(b) is B)