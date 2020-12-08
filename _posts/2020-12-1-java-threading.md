---
layout:     post
title:      协程 线程 进程 程序
subtitle:   协程 线程 进程 程序
date:       2020-12-01
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - java
---


- 协程

        单线程内函数函数级跳转，python 可通过yield关键字 和 next(func)方法实现 也有greenlet gevent 等模块实现协程  
        携程在函数间跳转时会保留现场上下文信息，然后跳转到另外一个函数，一般跳出跳回原函数时机由用户程序控制如 greenlet ,也可由模块通过算法判断跳出跳回时机 如gevent  
- 线程

        程序最小的执行的单位，一个程序可以有多个进程，并且每个进程可以有多个线程。拥有相同父进程的多个线程间共享一片内存，所以使用多线程时无需为资源共享设计方法，但需要考虑线程安全。  
        多个线程在多核处理器上可以并行执行。  
- 进程

        一个程序可以创建多个进程，不同进程间资源隔离，所以如需共享资源，可以借助管道 pip queue socket等方法实现。多个进程可以在多CPU机器上并行执行。  
- 程序

        指含有指令和数据的文件
- 使用时机

        三种方法用于对于程序内多模块在时序上有并行执行的需求的任务场景  
        一般功能高度独立的程序推荐用多进程方法，因为使用多线程，一个没处理的错误会同进程的所有线程崩溃。  
        对于高耦合性的模块，推荐使用多线程，因为多线程之间资源共享相对多进程较为简单，并且高耦合意味着要CPU频繁切换于多个线程，相比于多进程，多线程之间的切换开销要低。  
        对于协程，一般用于单线程内，IO操作，网络请求操作等耗时，并且不需要CPU守护的程序操作的的切换，用此来提高速度。  
        总之，一个程序可以有多个进程，一个进程可以有多个线程，一个线程可以在多个协程之间切换。      
- python 协程模块greenlet example

        from greenlet import greenlet
        import time
        
        def task_1():
            while True:
                print("--This is task 1!--")
                g2.switch()  # 切换到g2中运行
                time.sleep(0.5)
        
        def task_2():
            while True:
                print("--This is task 2!--")
                g1.switch()  # 切换到g1中运行
                time.sleep(0.5)
                
        if __name__ == "__main__":
            g1 = greenlet(task_1)  # 定义greenlet对象
            g2 = greenlet(task_2)
            
            g1.switch()  # 切换到g1中运行    
- python 协程模块gevent example

        import gevent
        def task_1(num):
            for i in range(num):
                print(gevent.getcurrent(), i)
                gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep
        def task_2(num):
            for i in range(num):
                print(gevent.getcurrent(), i)
                gevent.sleep(3)
        
        def task_3(num):
            for i in range(num):
                print(gevent.getcurrent(), i)
                gevent.sleep(6)
        
        if __name__ == "__main__":
            g1 = gevent.spawn(task_1, 5)  # 创建协程
            g2 = gevent.spawn(task_2, 5)
            g3 = gevent.spawn(task_3, 5)
        
            g1.join()  # 等待协程运行完毕
            g2.join()
            g3.join()

- 解决方法

        将需要同步的资源放在主函数内，如果程序没有主函数，建议创建一个主函数，然后使用 if \__name\__=="__mian__":main() 语法调用



