import os, re

current_path = './leetcode/'
line_count = 0
file_count = 0

def get_lines(current_path):
    global line_count
    global file_count
    for members in os.listdir(current_path):
        if members == '__pycache__' or members == './.idea' or members == './.git':
            continue
        temp_path = current_path + '/' + members
        if re.match(r'^\./\.', temp_path):
            continue
        if os.path.isfile(temp_path):
            try:
                file_count += 1
            except UnicodeDecodeError as e:
                pass
        else:
            get_lines(temp_path)

if __name__ == '__main__':
    for members in os.listdir(current_path):
        temp_path = current_path + members
        if os.path.isfile(temp_path):
            try:
                file_count += 1
                print(temp_path)
            except UnicodeDecodeError as e:
                pass
        elif os.path.isdir(temp_path):
            get_lines(temp_path)
    print('total file: {}'.format(file_count))