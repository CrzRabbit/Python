for d in range(1, 5):
    print(repr(d).rjust(2), repr(pow(d, 2)).rjust(2), end="")
    print(repr(pow(d, 3)).rjust(4))

for d in range(1, 5):
    print("{0:2d}{1:3d}{2:4d}".format(d, pow(d, 2), pow(d, 3)))

table = {"one" : 1, "two" : 2, "three" : 3}
print(table)
print("one: {0[one]:d} two: {0[two]:d} three: {0[three]:d}".format(table))
print("one: {one:d} two: {two:d} three: {three:d}".format(**table))