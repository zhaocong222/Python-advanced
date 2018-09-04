class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    def __init__(self,name):
        print("in init")
        self.name = name

#new 是用来控制对象的生成过程，在对象生成之前
if __name__ == "__main__":
    user = User(name="boddy")