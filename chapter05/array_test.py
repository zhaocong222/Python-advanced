#array,deque
#数组－》连续的内存空间
import array
#array和list的一个重要区别，array只能存放指定的数据类型
my_array = array.array("i")
my_array.append(1)

#TypeError: an integer is required (got type str)
#my_array.append("abc")