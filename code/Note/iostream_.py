def print_line(n=40):
    print(n * '=')

for d in range(1, 5):
    print(repr(d).rjust(2), repr(pow(d, 2)).rjust(2), end="")
    print(repr(pow(d, 3)).rjust(4))

for d in range(1, 5):
    print("{0:2d}{1:3d}{2:4d}".format(d, pow(d, 2), pow(d, 3)))
print_line()

table = {"one" : 1, "two" : 2, "three" : 3}
print(table)
print("one: {0[one]:d} two: {0[two]:d} three: {0[three]:d}".format(table))
print("one: {one:d} two: {two:d} three: {three:d}".format(**table))
print_line()

from io import StringIO

sio = StringIO()
sio.write('wefefwgweg')
print(sio.getvalue())
sio1 = StringIO('13')#初始化的时候设置内容
print(sio1.getvalue())
print_line()

from io import BytesIO

bio = BytesIO()
bio.write('中文'.encode('utf-8'))
print(bio.getvalue())
bio1 = BytesIO('英文'.encode('utf-8'))
print(bio1.getvalue())
print_line()

