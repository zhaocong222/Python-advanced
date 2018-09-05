#多线程编程 对于io操作来说，多进程和多线程性能差别不大
#1.通过thread类实例化

import time
import threading

def get_detail_html(url):
    #爬取文章详情页
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    # 爬取文章列表页
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html,args=("",))
    thread2 = threading.Thread(target=get_detail_url,args=("",))


    '''
    start_time = time.time()
    thread1.start()
    thread2.start()
    print("last time: {}".format(time.time() - start_time))
    '''

    '''
    上述代码段结果
    get detail html started
    get detail url started
    last time: 0.0003833770751953125
    get detail html end
    get detail html end
    
    这里last time 0.0003833770751953125, 因为 thread1和thread2进程开始执行了，
    print一行代码会由主进程继续执行，因此得到此结果
    主线程执行完程序等待子线程执行完成
    改造上述代码
    '''

    #将thread1和thread2设置为守护线程，意思就是说当主线程执行完退出后，直接将守护线程也关闭
    '''
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    print("last time: {}".format(time.time() - start_time))
    '''

    #最终改进
    start_time = time.time()
    thread1.start()
    thread2.start()

    #将thread1和thread2阻塞，thread1和thread2逻辑全部运行完后，主线程才会继续执行
    #执行时间为子线程内　最大执行时间
    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

