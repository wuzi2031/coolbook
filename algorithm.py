# 展开数组
def exportList(ls):
    return sum([exportList(x) if type(x) is list else [x] for x in ls], [])


def li(ls, tem=[]):
    for l in ls:
        if type(l) is list:
            li(l, tem)
        else:
            tem.append(l)
    return tem


# 二分查找
def twoSerch(ls, x, low, hight):
    if (low <= hight):
        mid_index = int((low + hight) / 2)
        mid = ls[mid_index]
        if mid == x:
            return mid_index
        elif mid < x:
            return twoSerch(ls, x, mid_index + 1, hight)
        elif mid > x:
            return twoSerch(ls, x, low, mid_index - 1)
    else:
        print(-1)
        return -1


# 快速排序
def quickSort(ls):
    if (ls == []):
        return ls
    else:
        first = ls[0]
        less = quickSort([x for x in ls if x < first])
        more = quickSort([x for x in ls if x > first])
        return less + [first] + more


if __name__ == "__main__":
    print(li([1, 3, [5, 6, [9, 10], [11, [12, [13, 14]]], 15]]))
    index = twoSerch([1, 4, 5, 6, 8, 9, 17], 4, 0, 6)
    print(quickSort([2, 1, 4, 89, 3, 6]))
