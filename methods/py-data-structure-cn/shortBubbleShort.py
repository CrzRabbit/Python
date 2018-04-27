
def shortBubbleShort(list):
    exchange = True
    num = len(list) - 1
    while num > 0 and exchange:
        exchange = False
        for i in range(0, num):
            if list[i] > list[i + 1]:
                list[i] = list[i] ^ list[i + 1]
                list[i + 1] = list[i] ^ list[i + 1]
                list[i] = list[i] ^ list[i + 1]
                exchange = True
        num -= 1
    return list

if __name__ == '__main__':
    list = [5, 9, 8, 48, 1, 78]
    print(shortBubbleShort(list))