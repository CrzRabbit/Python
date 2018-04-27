#
def moveTower(height, fromH, toH, withH):
    if height == 1:
        moveDisk(fromH, toH)
    else:
        moveTower(height - 1, fromH, withH, toH)
        moveDisk(fromH, toH)
        moveTower(height - 1, withH, toH, fromH)

def moveDisk(fromH, toH):
    print('move {0} to {1}'.format(fromH, toH))

if __name__ == '__main__':
    moveTower(2, 1, 3, 2)