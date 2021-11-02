def cycle(lst, n):
    if n > len(lst) - n:
        return lst
    else:
        lst.insert(0, lst.pop())
        return cycle(lst, n+1)

def test():

    lst = [1,2,3,4,5,6,7,8,9,10]
    # print(cycle(lst, 3))
    assert cycle(lst, 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

test()