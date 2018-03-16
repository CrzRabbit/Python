
def mergesort(list, l, h):
    if l == h - 1:
        return
    if l == h - 2:
        if list[l] > list[list.__len__() - 1]:
            list[l] = list[l] ^ list[list.__len__() - 1]
            list[list.__len__() - 1] = list[l] ^ list[list.__len__() - 1]
            list[l] = list[l] ^ list[list.__len__() - 1]
        return

    listl = list[l: int((l + h) / 2)]
    listr = list[int((l + h) / 2): h]
    list = []

    mergesort(listl, 0, listl.__len__())
    mergesort(listr, 0, listr.__len__())

    print(listl, listr)

    m = 0
    n = 0
    for i in range(l, h):
        if (n >= listr.__len__()) or ((m < listl.__len__()) and (listl[m] <= listr[n])):
            list.append(listl[m])
            print(listl[m])
            m += 1
            continue
        if (m >= listl.__len__()) or ((n < listr.__len__()) and (listr[n] <= listl[m])):
            list.append(listr[n])
            print(listr[n])
            n += 1
            continue

list = [25, 5, 23 , 99, 85, 5, 8]
mergesort(list, 0, list.__len__())
print(list)