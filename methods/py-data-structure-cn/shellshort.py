
def shellShort(list):
    step = len(list) // 2
    while step > 0:
        for i in range(0, step):
            insertSort(list, i, step)
        step = step // 2

def insertSort(list, l, step):
    le = len(list)
    index = l + step
    while index < le:
        curvalue = list[index]
        tempindex = index - step
        while tempindex >= 0:
            if curvalue < list[tempindex]:
                list[tempindex + step] = list[tempindex]
            else:
                break
            tempindex -= step
        list[tempindex + step] = curvalue
        index += step

if __name__ == '__main__':
    list = [5, 9, 8, 48, 1, 78, 78, 4, 922, 7]
    shellShort(list)
    print(list)