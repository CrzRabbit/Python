
def insertsort(list):
    for index in range(1, len(list)):
        currenvalue = list[index]
        position = index
        while position > 0 and list[position - 1] > currenvalue:
            list[position] = list[position - 1]
            position -= 1
        list[position] = currenvalue
    return list

if __name__ == '__main__':
    list = [5, 9, 8, 48, 1, 78]
    print(insertsort(list))