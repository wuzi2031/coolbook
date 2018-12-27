li = (lambda: x for x in range(10))
ll = [lambda: x for x in range(10)]
for l in li:
    print(l())
for l in ll:
    print(l())
xx = ['aa', 'bb']
yy = ['cc', 'dd']
re = [{x: y} for x in xx for y in yy]
print(re)
print(dict(zip(xx, yy)))
for r in map(lambda x: x + "1", xx):
    print(r)
var = 'ss'


def test():
    print(var)


var = 'dd'
test()

a = [1, 2, 3, 4, 5]
b = [3, 4, 7, 8, 9]
tem = []
a.extend(b)
print(set(sorted(a)))


import pyclbr


def getModuleCls(module_name):
    return [x for x in pyclbr.readmodule(module_name).keys()]
