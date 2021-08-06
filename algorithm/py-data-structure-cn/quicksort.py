import sys
sys.setrecursionlimit(1000000)

def quicksort(list, l, h):
    temp = list[l]
    lt = l
    ht = h
    while lt < ht:
        if list[ht] < temp:
            list[lt] = list[ht]
            lt += 1
            while lt < ht:
                if list[lt] > temp:
                    list[ht] = list[lt]
                    ht -= 1
                    break
                else:
                    lt += 1
        else:
            ht -= 1
    list[lt] = temp
    print(list)
    if l <= lt - 1:
        quicksort(list, l, lt -1)
    if lt + 1 <= h:
        quicksort(list, lt + 1, h)
    return

list = [25, 5, 23 , 99, 85, 5, 8]
quicksort(list, 0, list.__len__() - 1)
print(list)
