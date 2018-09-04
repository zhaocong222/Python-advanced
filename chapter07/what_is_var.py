#python和java中变量本质不一样,python变量实质上是一个指针 int str,便利贴

#1. 生成一个int内存空间 ,先生成对象１
#2. 然后把a贴在1上面
a = 1
#3. 当然a可以贴在任意上面
a = "abc"
a = [1,2,3]
#把a贴到了b上
b = a
b.append(4)

print(a)
print(id(a),id(b))
print(a is b) #是否是同一个对象 true

del a  #销毁a
print(b) #[1, 2, 3, 4]