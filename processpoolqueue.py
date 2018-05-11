from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
import time, os


class ProcessDataSync:
    def __init__(self):
        m = Manager()
        self.q = m.Queue(1)  # queue线程安全
        self.x = 0
        self.q.put(0)
        self.proCount = 10

    def add(self, q):
        r = q.get(block=True)
        r += 1
        time.sleep(1)
        print("pid: " + str(os.getpid()) + " add: " + str(r))
        q.put(r)

    def reduce(self, q):
        r = q.get()
        r -= 1
        print("pid: " + str(os.getpid()) + " reduce: " + str(r))
        q.put(r)

    def addx(self):
        # time.sleep(1)
        self.x += 1
        print("add: " + str(self.x))

    def reducex(self):
        # time.sleep(1)
        self.x -= 1
        print("add: " + str(self.x))

    def callBack(self, result):
        pass

    def processAdd(self):
        with ProcessPoolExecutor(max_workers=self.proCount) as pr:
            for i in range(self.proCount):
                pr.submit(self.add, self.q)
                pr.submit(self.reduce, self.q)
                # pr.submit(self.addx)


if __name__ == '__main__':
    p = ProcessDataSync()
    p.processAdd()
