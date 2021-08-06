
def binarySearch(list, item):
    l = 0
    h = len(list) - 1
    found = False

    while l < h and not found:
        mid = (l + h) / 2
        if list[mid] == item:
            found = True
        else:
            if list[mid] < item:
                h = mid - 1
            else:
                l = mid + 1
    return found

if __name__ == '__main__':
    pass