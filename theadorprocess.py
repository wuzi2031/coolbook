from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time, functools


def feachTime(fun):
    @functools.wraps(fun)
    def wapper(*args, **kwargs):
        s = time.clock()
        fun(*args, **kwargs)
        e = time.clock()
        print(fun.__name__ + ":" + str(e - s))

    return wapper


class PoolTest:
    # @feachTime #加上无回调结果
    def add(self, x, y):
        for i in range(100000000):
            x + y
        return x + y
    def callback(self,feature):
        print(feature.result())
    def theadMulAdd(self):
        t = ((1, 2), ('q', 'r'), ('1', 'g'))
        with ThreadPoolExecutor(max_workers=len(t)) as executor:
            for i in t:
                executor.submit(self.add, i[0], i[1]).add_done_callback(self.callback)
                # re=executor.submit(self.add, i[0], i[1])
                # print(str(i) + str(re.result()))

    def processMulAdd(self):
        t = ((1, 2), ('q', 'r'), ('1', 'g'))
        with ProcessPoolExecutor(max_workers=len(t)) as executor:
            for i in t:
                executor.submit(self.add, i[0], i[1]).add_done_callback(self.callback)
                # re=executor.submit(self.add, i[0], i[1])
                # print(str(i)+str(re.result()))


if __name__ == '__main__':
    t = PoolTest()
    t.theadMulAdd()
    t.processMulAdd()
