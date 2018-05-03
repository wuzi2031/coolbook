from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time
from threading import current_thread
def foo():
    time.sleep(1)
    print('%s  %s from foo'%(os.getpid(),current_thread().getName()))
    return 'foo'
def bar():
    time.sleep(2)
    print('%s  %s from bar' % (os.getpid(),current_thread().getName()))
    return 'bar'
if __name__ == '__main__':
    t1=time.time()
    executor=ProcessPoolExecutor()
    print('executor',executor)
    future1=executor.submit(foo)
    future2=executor.submit(bar)
    print(future1,future2)
    executor.shutdown()
    print(future1.result())
    print(future2.result())
    print(time.time()-t1)