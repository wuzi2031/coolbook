import os

print(os.path.join("a/v", "bvv"))
print("a".join("bbb"))


class A:
    str = ""


class B(A):
    str = "dfad"


# print(A.str)
# print(B.str)
a = {'dd': 'dd'}
b = {}
a.update(b)
print(a)
print()