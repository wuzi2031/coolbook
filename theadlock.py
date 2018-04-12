import threading
import time


def run(n):
    global  num
    lock.acquire()      # 同一时间只有一个线程获取锁
    print("start task and lock acquire",n)
    num += 1
    time.sleep(1)
    print("task done and lock release" ,n)
    lock.release()


lock = threading.Lock()
num = 0
t_job = []
for i in range(3):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_job.append(t)

for each in t_job:
    each.join()

print("main thread done........")