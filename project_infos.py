import os, re

current_path = './'
line_count = 0
file_count = 0

def get_lines(current_path):
    global line_count
    global file_count
    #print(current_path)
    for members in os.listdir(current_path):
        if members == '__pycache__' or members == './.idea' or members == './.git':
            continue
        temp_path = current_path + '/' + members
        if re.match(r'^\./\.', temp_path):
            continue
        if os.path.isfile(temp_path):
            try:
                file = open(temp_path)
                lines = file.readlines()
                line_count += lines.__len__()
                file.close()
                print(temp_path + ': {}'.format(lines.__len__()))
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
                file = open(temp_path)
                lines = file.readlines()
                line_count += lines.__len__()
                file.close()
                print(temp_path + ': {}'.format(lines.__len__()))
                file_count += 1
            except UnicodeDecodeError as e:
                pass
        else:
            get_lines(temp_path)
    print('')
    print('total file count: {}'.format(file_count))
    print('total line count: {}'.format(line_count))