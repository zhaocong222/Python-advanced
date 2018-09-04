#set集合　fronzenset(不可变集合) 无序,不重复
s = set('abcde')
s.add('x')
print(s)

#s = set(['a','b','c','d','e'])
#s = {'a','v','c'}
print(type(s))

another_set = set("def")
s.update(another_set)
print(s)

# 取差集 -> differebce 和 减


#无法修改 frozenset可以作为dict的key
s = frozenset("abcde")


if 'c' in s:
    print("c am in set")

#1. dict的key或者set的值 都必须是可以
#2. dict的内存花销大，但是查询速度快
#3. dict的存储顺序和元素添加顺序有关