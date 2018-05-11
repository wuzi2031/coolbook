import re
s="""
https://www.
baidu.com
vsfgafgsfg
http://fsdfsd.com"fdfsf
"""
rex=re.compile(r'https?://.*com')
c=rex.findall(s)

names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
print(sorted(names[0].split()[0],reverse=True))
print(sorted(names,key=lambda name : name.split()[-1]))
def ceshi(self):
    pass

print(ceshi.__name__)
print(re)
testDict = {i:i*i for i in range(2,10)}
print(testDict)
testList = [i for i in range(1,5)]
testList.append(4)
for i,value in enumerate(testList):
    print(str(i)+":"+str(value))
print(testList)
testSet = {i for i in range(1,5)}
testSet.add(4)
print(testSet)
str="abcdefghijk"
print(str[::-1])
ls=[1,1,1,1,2,2,2,3,3]
print(ls.count)
print(dir(ls))
print(max(set(ls),key=ls.count))
print(ls)
mcase = {'a': 10, 'b': 34}
print({key:mcase[key] for key in mcase})
print([mcase[key] for key in mcase if key=='a'])
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
print(mcase_frequency)
# 例1:  过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
str_l = ['a','ab','abc','abcd','abcde']
print([s.upper() for s in str_l if len(s)>3])
# 例2:  求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
print([(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1])
# 例3:  求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
M = [[1,3,3],[4,5,6],[7,8,9]]
print([i for ls in M for i in ls if i in (3,6,9)])
print([i//2 if i%2==0 else i for i in range(100) if i % 3 == 0 ])  #三元运算肯定要返回个值
print(tuple(i for i in range(3)))
print(list("adfsd"))
print("dfs"+'fsd')
print("123".join(('d','d')))

print([x*2 for x in range(1,11)])
print(list(map(lambda x:x*2,range(1,11))))
wordlist = ["scala", "akka", "play framework", "sbt", "typesafe"]

tweet = "This is an example tweet talking about scala and sbt."

print(list(filter(lambda x: x in tweet.split(), wordlist)))