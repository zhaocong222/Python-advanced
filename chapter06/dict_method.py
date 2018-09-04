a = {
        "boddy1":{"company":"imooc"},
        "boddy2":{"company": "imooc2"},
}

#clear
#a.clear()
#pass

#copy,返回浅拷贝
new_dict = a.copy()
new_dict["boddy1"]["company"] = "immooc3"

#浅拷贝的问题，修改new_dict,a也改变了->浅拷贝只是改变指向位置
print(new_dict)
print(a)

