class GeneratorTest:
    def oddNumber(self,maxNum,minNum=0):
        if(minNum<0 or maxNum<0):
            raise Exception('不能小于0')
        if(maxNum<minNum):
            raise Exception('最大值不能小于最小值')
        for i in range(minNum,maxNum+1):
            if(i%2!=0):
                yield i
# if __name__=='__main__':
#     gen = GeneratorTest()
#     re=gen.oddNumber(12,3)
#     print(next(re))
#     print(next(re))
#     for i in re:
#         print(i)

def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

if __name__=='__main__':
    c = countdown(5)
    for x in c:
        print(x)
        if x == 5:
            c.send(3)