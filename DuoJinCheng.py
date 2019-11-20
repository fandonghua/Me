from multiprocessing import Process
import multiprocessing,time

#执行子进程的代码
def test():
    time.sleep(2)
    print('我是子进程')
#执行主程序
def main ():
    print('主进程开始')
    for i in range(5):
        p = Process(target=test(),args=(1,))#实例化进程类
        p.start()#启动子进程
if __name__ == '__main__':
    main()
    print('主进程结束')
    print(multiprocessing.current_process())
    print(multiprocessing.context)