import os, re

current_path = './leetcode/'
name = '匹配'

def findFiles(current_path):
    for members in os.listdir(current_path):
        if members == '__pycache__' or members == './.idea' or members == './.git':
            continue
        temp_path = current_path + '/' + members
        if re.match(r'^\./\.', temp_path):
            continue
        if os.path.isfile(temp_path) and re.search(r'{}'.format(name), temp_path.split('/')[-1]):
            print(temp_path)
        elif os.path.isdir(temp_path):
            findFiles(temp_path)

if __name__ == '__main__':
    for members in os.listdir(current_path):
        temp_path = current_path + members
        if os.path.isfile(temp_path) and re.search(r'{}'.format(name), temp_path.split('/')[-1]):
            print(temp_path)
        elif os.path.isdir(temp_path):
            findFiles(temp_path)