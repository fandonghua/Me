from multiprocessing import Process
import time
import os


class Subprocess(Process):
    def __init__(self,interval,name= ''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name
    def run(self):
        print('子进程%s开始执行，父进程为%s' % (os.getpid(), os.getppid()))
        t_start = time.time()  # 计时开始
        time.sleep(self.interval)
        t_end = time.time()  # 计时结束
        print("子进程%s执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))

if __name__ == '__main__':
    print('----------父进程开始执行-------------------')
    print('父进程pid:%s'% os.getpid())
    p1 =Subprocess(interval=5,name='mrsoft')
    p2 =Subprocess(interval=6)
    p1.start()
    p2.start()
    print('p1.is_alive=%s'%p1.is_alive())
    print('p1.is_alive=%s'%p2.is_alive())
    #输出p1和p2进程的别名和ID
    print('p1.name=%s'%p1.name)
    print('p1.pid=%s'%p1.pid)
    print('p2.name=%s'%p2.name)
    print('p2.pid=%s'%p2.pid)
    print('---------等待子进程------------------')
    p1.join()
    p2.join()
    print('----------父进程执行结束---------------')
