class Date:
    #构造函数
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year),int(month),int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year),int(month),int(day))


    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

if __name__ == "__main__":
    new_day = Date(2018,12,31)
    new_day.tomorrow()
    print(new_day)

    #2018-12-31
    date_str = "2018-12-31"
    #year,month,day = tuple(date_str.split("-"))
    #print(year,month,day)

    #用staticmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    #用classmethod完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)