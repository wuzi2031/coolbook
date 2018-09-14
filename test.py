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
var='dd'
test()
