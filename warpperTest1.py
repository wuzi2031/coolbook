from warpperTest import DefWapper
class wTest:
    def __init__(self,name):
        self.name=name
    @DefWapper.timeit2(lev='error')
    def func1(self):
        print("func1 test")
    @DefWapper.timeit1
    def func2(self):
        print("func2 test")
w = wTest('wzm')
print(w.__dict__)
w.func1()
w.func2()