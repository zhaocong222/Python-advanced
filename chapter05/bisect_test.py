import bisect

#用来处理已排序的序列,用来维持已排序的序列，升序
#二分查找实现
inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,2)
bisect.insort(inter_list,5)
bisect.insort(inter_list,1)
bisect.insort(inter_list,6)

#元素应该插入的位置
print(bisect.bisect_left(inter_list,3))
print(bisect.bisect_right(inter_list,3))

#print(inter_list)
