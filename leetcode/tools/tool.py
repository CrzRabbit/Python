import re, os

def showNotCompleted():
    os.chdir('..')
    for item in os.listdir('.'):
        if re.search(r'_XXX\.py', item):
            print(item)

if __name__ == '__main__':
    showNotCompleted()