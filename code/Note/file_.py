import os

file = open("1.txt", "r+")
str = file.read()
print(str)

file.close()
file = open("1.txt", "r+")

str = file.readline()
print(str)

file.close()
file = open("1.txt", "r+")

str = file.readlines()
print(str)

file.close()
file = open("1.txt", "r+")

num = file.write("How are you")
print(num)

file.close()
file = open("1.txt", "r+")

str = file.readline()
print(str)

file.close()
file = open("1.txt", "r+")

print(file.tell())

file.close()
file = open("1.txt", "r+")

file.seek(10)
str = file.readline()
print(str)

file.close()

print([x for x in os.listdir('..') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])