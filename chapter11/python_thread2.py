#多线程编程 对于io操作来说，多进程和多线程性能差别不大
#1.通过thread类实例化

import time
import threading


#2.通过继承Thread实现多线程 (逻辑复杂时此方案)
class GetDetailHtml(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()
    thread1.start()
    thread2.start()

    # 将thread1和thread2阻塞，thread1和thread2逻辑全部运行完后，主线程才会继续执行
    # 执行时间为子线程内　最大执行时间
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))
