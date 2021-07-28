# codeing:-*-UTF-8-*-
import os, re

current_path = './leetcode/'
name = 'XXX'

def findFiles(current_path):
    for members in os.listdir(current_path):
        if members == '__pycache__' or members == './.idea' or members == './.git':
            continue
        temp_path = current_path + '/' + members
        if re.match(r'^\./\.', temp_path):
            continue
        # if os.path.isfile(temp_path):
        #     f = open(temp_path)
        #     try:
        #         if f.readlines().__len__() < 5:
        #             print(temp_path)
        #     except Exception as e:
        #         pass
        if os.path.isfile(temp_path) and re.search(r'{}'.format(name), temp_path.split('/')[-1]):
            print(temp_path)
            pass
        elif os.path.isdir(temp_path):
            findFiles(temp_path)

if __name__ == '__main__':
    for members in os.listdir(current_path):
        temp_path = current_path + members
        if os.path.isfile(temp_path) and re.search(r'{}'.format(name), temp_path.split('/')[-1]):
            print(temp_path)
        elif os.path.isdir(temp_path):
            findFiles(temp_path)