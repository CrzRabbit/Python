from functools import reduce, wraps
from operator import itemgetter
import time
import functools

def print_line(n = 30):
    print("=" * n)
#默认参数
def add_end(l = []): #默认参数必须是不可变对象
    l.append("END")
    return l

print(add_end()) #"END"
print(add_end()) #"END" "END"
print_line()

#可变参数
def sum(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

list = [1, 2, 3, 4, 5, 6]
print(sum(*list))
print(sum(1, 2, 3))

print_line()
#关键字参数
def person_info(name, age, **kw):
    print("name: {0} \nage:{1} \nother:{2}".format(name, age, kw))
person_info("wjc", 22)
person_info("w", 22, job = "coding")
person_info("w", 22, job = "coding", weight =55, hobby = "computer game")
print_line()

#命名关键字参数
def student_info(name, age, *, school = "XiangShui Middle School", weight):
    print("name: {0} \nage: {1} \nother: {2}, {3}".format(name, age, school, weight))
#or
'''
def student_info(name, age, *args, school = "XiangShui Middle School", weight):
    print("name: {0} age: {1} other: {2}, {3}".format(name, age, school, weight))
'''
# error:no keyword-only argument 'weight'
# student_info("wjc", 22)
student_info("wjc", 22, weight = 55)
print_line()

#参数组合 尽量不要使用太多组合，否则接口很难理解清楚
def food_info(name, price, type = "cold", *description, location, **kw):
    print("name: {0} \nprice: {1} \ntype: {2} \ndescription: {3} \nlocation: {4} \nkw: {5}".format\
              (name, price, type, description, location, kw))
food_info("rice", 1, "hot", "just so so" , location = "China", taste = "good")
print_line()

#高阶函数map/reduce
def power(x, n = 2):
    ret = 1
    while n > 0:
        ret *= x
        n -= 1
    return ret
print("map:")
relt = map(power, [1, 2, 3, 4])
for n in relt:
    print(n)
print_line()
def add(x, y):
    return x + y
print("reduce:")
print(reduce(add, [1, 2, 3, 4]))
print_line()

#实战
DIGIT = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
def char2num(c):
    return DIGIT[c]

def str2num(str):
    return reduce(lambda x, y:x * 10 + y, map(char2num, str))

str = "134532"
print(str)
print(str2num(str))
print_line()

#高阶函数filter
def is_odd(n):
    return not n % 2

list = filter(is_odd, [1, 2, 3, 4, 5])
for n in list:
    print(n)
print_line()

#实战 获取素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 20:
        print(n)
    else:
        break
print_line()

def normalize(name):
    name = name.lower()
    return name[0].upper() + name[1:]

L1 = ['adam', 'LISA', 'barT', 'hgoiOIHGWihgwiOIHGOIgihgw']
for str in map(normalize, L1):
    print(str)
print_line()

def prod(L):
    return reduce(lambda x, y: x * y, L)

list = [1, 2, 3, 4, 5]
print(prod(list))
print_line()

D = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
def c2n(c):
    return D[c]

point = 10
def get_float(x, y):
    global point
    if y == '.':
        point = 1
        return x
    if point <= 1:
        point /= 10
        return x + y * point
    return x * point + y

def str2float(str):
    return reduce(get_float, map(c2n, str))

str = "111.3233"
print(str)
print(str2float(str))
print_line()

#sorted
print(sorted([10, -5, -9, -11, 20], key = abs, reverse = True))

L = [('Bob', 75, 1), ('Adam', 75, 2), ('Bart', 75, 3), ('Lisa', 75, 4)]
print(sorted(L, key=itemgetter(0)))
print(sorted(L, key=itemgetter(1)))
print(sorted(L, key=itemgetter(1, 2)))
print_line()

#返回函数
# def createCounter():
#     def c(i):
#         def counter():
#             return i
#     i = 0
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA())
#print_line()

#装饰器
def now():
    print(time.ctime(time.time()))

func = now
func()

def decorator(func):
    def wrapper(*args, **kw):
        print("{0}{1} {2}".format(func.__name__, "()", "executed"))
        return func(*args, **kw)
    return wrapper

func = decorator(now)
func()

def log(txt):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("{0}{1} {2}".format(func.__name__, "()", txt))
            return func(*args, **kw)
        return wrapper
    return decorator
func = log("finished")(now)
func()

@functools.wraps(func)
def decorator(func):
    def wrapper(*args, **kw):
        time1 = time.time()
        for i in range(0, 10000):
            func(*args, **kw)
        time2 = time.time()
        print(time2 - time1)
    return wrapper
func = decorator(now)
func()
print_line()
#偏函数
int2 = functools.partial(int, base=2)
print(int2("100"))

max2 = functools.partial(max, 10)#将10作为max的第一个参数
print(max2(2, 6, 3))


import logging

def user_logging(level):
    def derector(func):
        def wrapper(*args, **kw):
            if level == "warn":
                logging.warn("{0} is running...".format(func.__name__))
            func(*args)
        return wrapper
    return derector

@user_logging(level = "warn")
def color(color = "red"):
    print("color is {0}".format(color))

color()
