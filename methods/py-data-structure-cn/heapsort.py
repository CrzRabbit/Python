
def buildheap(list, len):
    temp = int(len / 2)
    while temp >= 0:
        if((temp * 2 + 1) <= len and list[temp] < list[temp * 2 + 1]):
            list[temp] = list[temp] ^ list[temp * 2 + 1]
            list[temp * 2 + 1] = list[temp] ^ list[temp * 2 + 1]
            list[temp] = list[temp] ^ list[temp *2 + 1]

        if(list[temp] < list[temp * 2]):
            list[temp] = list[temp] ^ list[temp * 2]
            list[temp * 2] = list[temp] ^ list[temp * 2]
            list[temp] = list[temp] ^ list[temp * 2]
        temp -= 1

def heapsort(list, len):
    while len > 0:
        buildheap(list, len)
        list[0] = list[len] ^ list[0]
        list[len] = list[len] ^ list[0]
        list[0] = list[len] ^ list[0]
        len -= 1

list = [25, 5, 23 , 99, 85, 5, 8]
heapsort(list, list.__len__() - 1)
print(list)