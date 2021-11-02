'''implement a recursive function that cycles a list n times. 
cycling a list involves taking an element off the end of the list and adding it to the beginning. 
cycling abcde once returns eabcd. cycling it twice returns deabc. '''

def cycle(lst, n):
    if n < 1:
        return lst
    else:
        lst.insert(0, lst.pop())
        return cycle(lst, n-1)

def test():

    lst = [1,2,3,4,5,6,7,8,9,10]
    print(cycle(lst, 6))
    # assert cycle(lst, 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

test()