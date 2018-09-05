#semahore 是用于控制进入数量的锁
#文件读写，写一般只是用于一个线程写，读可以允许有多个

import threading
import time

class HtmlSpider(threading.Thread):

    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("get html text success")
        #爬取玩一个页面内容释放信号锁 sem值 +1
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        #这里创建了20个线程处理url,但是希望一次只并发3个
        for i in range(20):
            #每进来一个　内部sem 会减１，减到为0则锁住
            self.sem.acquire()
            html_thread = HtmlSpider("https://www.baidu.com",sem)
            html_thread.start()


if __name__ == "__main__":
    #一次允许３个并发
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()

    #执行代码，发现每次执行3个，然后再执行3个