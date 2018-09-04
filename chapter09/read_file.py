#读取大文件，文件只有一行数据,　空格分割形式
def myreadlines(f,newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(20)

        if not chunk:
            #说明已经读到了文件结尾
            yield buf
            break
        #如果读取的字符串中不包含{|} 则一直把字符串存到变量buf里
        buf += chunk



with open("input.txt") as f:
    for line in myreadlines(f,"{|}"):
        print(line)