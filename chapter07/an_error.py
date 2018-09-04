def add(a,b):
    a += b
    return a

if __name__ == "__main__":
    a = 1
    b = 2

    a = [1,2]
    b = [3,4]

    a = (1,2)
    b = (3,4)

    c = add(a,b)

    print(c)
    print(a,b)
