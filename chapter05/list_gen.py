#列表生成式
#1. 提取出1-20之间的奇数
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)

#利用列表生成式
odd_list = [i for i in range(21) if i % 2 == 1]
print(type(odd_list))
print(odd_list)

#2.逻辑复杂的情况 奇数平方
def handle_item(item):
    return item * item

odd_list = [ handle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

#生成器表达式 <class 'generator'>
odd_list = ( i for i in range(21) if i % 2 == 1)
print(type(odd_list))
print(odd_list.__next__())
print(odd_list.__next__())
print(odd_list.__next__())

oxx = list(odd_list)
print(type(oxx))
print(oxx)

#字典推导式
my_dict = {"boobby1":22,"bobby2":23,"immoc.com":5}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)

#集合推导式
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)