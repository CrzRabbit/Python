
def get_charge(list, charge):
    minnum = charge
    if charge in list:
        return 1
    for c in [l for l in list if l < charge]:
        curnum = 1 + get_charge(list, charge - c)
        if curnum < minnum:
            minnum = curnum

    return minnum

def get_charge1(coinValueList, charge, knownResult):
    minnum = charge
    if charge in coinValueList:
        return 1
    if knownResult[charge] != 0:
        return knownResult[charge]

    for i in [c for c in coinValueList if c < charge]:
        curnum = 1 + get_charge1(coinValueList, charge - i, knownResult)
        if curnum < minnum:
            minnum = curnum
            knownResult[charge] = minnum

        return minnum

def get_charge2(coinValueList, charge, coinCount, usedCoin):
    for cent in range(charge + 1):
        curcount = cent
        for i in [c for c in coinValueList if c < charge]:
            if coinCount[cent - i] + 1 < curcount:
                curcount = coinCount[cent - i] + 1
                usedCoin[cent] = i
        coinCount[cent] = curcount

if __name__ == '__main__':
    # print('get_charge: {0}'.format(get_charge([1, 5, 10, 25], 63)))
    # print('get_charge1: {0}'.format(get_charge1([1, 5, 10, 25], 63, [0] * 64)))
    coinCount = [0] * 64
    usedCoin = [0] * 64
    get_charge2([1, 5, 10, 21, 25], 63, coinCount, usedCoin)
    print(coinCount)
    print(usedCoin)