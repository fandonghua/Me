from multiprocessing import Process
import time
import os

#两个子进程将会调用的两个方法
def child_1(interval):
    print('子进程%s开始执行，父进程为%s'%(os.getpid(),os.getppid()))
    t_start = time.time() #计时开始
    time.sleep(interval)
    t_end = time.time()#计时结束
    print("子进程%s执行时间为'%0.2f'秒"%(os.getpid(),t_end-t_start))
def child_2(interval):
    print('子进程%s开始执行，父进程为%s'%(os.getpid(),os.getppid()))
    t_start = time.time() #计时开始
    time.sleep(interval)
    t_end = time.time()#计时结束
    print("子进程%s执行时间为'%0.2f'秒"%(os.getpid(),t_end-t_start))
if __name__ == '__main__':
    print('----------父进程开始执行-------------------')
    print('父进程pid:%s'% os.getpid())
    p1 = Process(target=child_1,args=(1,))
    p2 = Process(target=child_2,name='mrsoft',args=(2,))
    p1.start()
    p2.start()

    print('---------等待子进程------------------')
    p1.join()
    p2.join()
    #同时父进程任然往下执行，如果p2进程还在执行，将会返回true
    print('p1.is_alive=%s'%p1.is_alive())
    print('p1.is_alive=%s'%p2.is_alive())
    #输出p1和p2进程的别名和ID
    print('p1.name=%s'%p1.name)
    print('p1.pid=%s'%p1.pid)
    print('p2.name=%s'%p2.name)
    print('p2.pid=%s'%p2.pid)
    print('----------父进程执行结束---------------')







