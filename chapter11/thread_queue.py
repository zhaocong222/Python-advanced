# 多线程编程 对于io操作来说，多进程和多线程性能差别不大
import time
import threading
from chapter11 import variables


def get_detail_html():

    while True:
        if len(variables.detail_url_list):
            url = variables.detail_url_list.pop()

            #for url in detail_url_list:
            # 爬取文章详情页
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url():
    while True:
        # 爬取文章列表页
        print("get detail url started")
        time.sleep(2)
        for i in range(20):
            variables.detail_url_list.append("http://projectsedu.com/{id}".format(id=i))

        print("get detail url end")

#1.　线程通信方式 - 共享变量 global
#2.  传参
#ps: 通过共享变量并不是线程安全的操作，要加锁

#3. 利用queue

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)

    #启动10个线程处理url
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()

