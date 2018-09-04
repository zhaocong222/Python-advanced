class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    #魔法函数,可迭代类型
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ",".join(self.employee)


company = Company(["tom","bob","jane"])


'''
emploee = company.employee

for em in emploee:
    print(em)
'''

#直接使用魔法函数__getitem__ , for会取找__getitem__是否有__getitem__
for em in company:
    print(em)

print("\n")

#切片
company1 = company[:2]
for em in company1:
    print(em)

print(len(company))
print(len(company1))

#触发__str__
print(company)