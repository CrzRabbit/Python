
def mergesort(list):
    l = 0
    h = list.__len__()
    if l == h - 1:
        return list
    if l == h - 2:
        if list[l] > list[list.__len__() - 1]:
            list[l] = list[l] ^ list[list.__len__() - 1]
            list[list.__len__() - 1] = list[l] ^ list[list.__len__() - 1]
            list[l] = list[l] ^ list[list.__len__() - 1]
        return list

    listl = list[l: int((l + h) / 2)]
    listr = list[int((l + h) / 2): h]
    list = []

    listl = mergesort(listl)
    listr = mergesort(listr)

    m = 0
    n = 0
    for i in range(l, h):
        if (n >= listr.__len__()) or ((m < listl.__len__()) and (listl[m] <= listr[n])):
            list.append(listl[m])
            m += 1
            continue
        if (m >= listl.__len__()) or ((n < listr.__len__()) and (listr[n] <= listl[m])):
            list.append(listr[n])
            n += 1
            continue
    print(list)
    return list

list = [25, 5, 23 , 99, 85, 5, 8]
list = mergesort(list)
print(list)