my_list = []
my_list.append(1)
my_list.append("a")

a = [1,2]
#TypeError: can only concatenate list (not "tuple") to list
#c = a + (3,4)
c = a + [3,4]

# += 底层调用了extend方法， 内部实现 for in
a += (3,4)

print(c)
print(a)

a.extend(range(3))
a.extend((5,6,7))

print(a)