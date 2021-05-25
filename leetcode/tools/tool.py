import re, os

def showNotCompleted():
    os.chdir('..')
    for item in os.listdir('.'):
        if re.search(r'_XXX\.py', item):
            print(item)

def printMatrix(ret, s, p):
    line = ' ' * 8
    for j in range(len(p)):
        line += '{:^6s}'.format(p[j])
    print(line)
    for i in range(0, len(s) + 1):
        line = '  '
        if i > 0 and i < len(s) + 1:
            line = s[i - 1] + ' '
        for j in range(0, len(p) + 1):
            if ret[i][j]:
                line += 'True  '
            else:
                line += 'False '
        line += '\r\n'
        print(line)

def printMatrix(matrix):
    print('---')
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[0])):
            line += '{:^3}'.format(matrix[i][j])
        print(line)

if __name__ == '__main__':
    showNotCompleted()