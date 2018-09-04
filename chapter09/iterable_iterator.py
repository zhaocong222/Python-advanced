from collections.abc import Iterator

class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    #def __getitem__(self, item):
    #    return self.employee[item]

class MyIterator(Iterator):
    def __init__(self,employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #返回迭代值
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":
    company = Company(["tom","bob","jane"])
    #调用魔术方法__iter__
    my_iter = iter(company)
    '''
    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            pass
    '''
    for item in my_iter:
        print(item)