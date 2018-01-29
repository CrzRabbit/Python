# codeing:-*-UTF-8-*-
import types
from types import MethodType
from enum import Enum, unique

def print_line(n = 30):
    if n <0:
        print("=" * 30)
    else:
        print("=" * n)

class test:
    def __init__(self, name, age, job):
        self.name = name
        self.__age = age
        self.__job = job
    def __del__(self):
        print("don't kill me")
    def __deepcopy__(self, memodict={}):
        return test(self.name, self.__age, self.__job)
    def __copy__(self):
        return self
    def __str__(self):
        return "name: %s age:%d job:%s" % (self.name, self.__age, self.__job)

me = test("wjc", 22, "coding")
#深拷贝
mec = me.__deepcopy__()
mec.name = "wjcc"
#浅拷贝
mec1 = me.__copy__()
mec1.name = "wjc1"
print(me)
print(mec)
print(mec1)
print_line()
#多态
class Animal:
    def run(self):
        print('Animal is running~')
class Dog(Animal):
    def run(self):
        print('Dog is running~')

class People:
    def run(self):
        print('People is running~')
class Doctor(People):
    def run(self):
        print('Doctor is running~')

def run(object):
    object.run()

run(People())
run(Animal())
run(Dog())
run(Doctor())
print_line()
#获取类型
print(type(123) == type(23543))
print(type(123) == int)
print(type('abc') == str)
print_line()
print(type(lambda x: x * x))
print(type(run))
print_line()
print(dir('abc'))
print(dir(test))
print(setattr(test, 'name', 'test'))
print(getattr(test, 'name'))
print(hasattr(test, 'name'))
print(dir(test))
print_line()

class Student:
    count = 0#类的属性
    def __init__(self, name = 'student'):
        self.name = name
        Student.count += 1
Student()
Student()
print(Student.count)
print_line()

class Student:#定一个类，为实例动态添加属性/方法
    pass

def set_age(self, age):#定义要添加的方法
    self.age = age

s1 = Student()
s1.name = 'w'#为实例添加属性
s1.set_age = MethodType(set_age, s1)#为实例添加方法
s1.set_age(23)
print(s1.age)

s2 = Student()
# print(s2.name)#s1绑定的属性s2不能使用
# s2.set_age(23)#方法同样不能使用

def set_score(self, score):#定义为类添加的方法
    self.score = score

Student.set_score = set_score#为类添加方法
s1.set_score(100)
s2.set_score(99)
print(s1.score)
print(s2.score)
print_line()

class Student(object):
    __slots__ = ('name', 'age')#__slots__指定可以动态添加的属性

s1 = Student()
s1.name = 'wjc'
s1.age = 23
# s1.score = 88#__slots__未指定,不能添加
print(s1.name)
print(s1.age)
print_line()

class Girl(Student):
    pass

g1 = Girl()
g1.score = 99#__slots__不作用于子类
print(g1.score)
print_line()

# @property的使用
class Student(object):
    @property
    def score(self):
        return  self.score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 adn 100')
        self.score = value
print_line()

#type动态创建类
def fn(self, name='world'):
    print('hello, {0}'.format(name))

Hello = type('Hello', (object,), dict(hello=fn))
hello = Hello()
hello.hello()
print_line()

#metaclass元类
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add('l') #成功为类添加了add方法
print(l)
print_line()

#用元类实现ORM,全称“Object Relational Mapping”，即对象-关系映射，
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaClass(type):
    def __new__(cls, name ,bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Find Model:{0}'.format(name))
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Find Mapping: {0} ====> {1}'.format(k, v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise ValueError('Model object has no attribute {0}'.format(key))

    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = "insert into {0} ({1}) values ({2})".format(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {0}'.format(sql))
        print('Args: {0}'.format(args))

class User(Model):
    id = IntegerField('id')
    pwd = StringField('pwd')
    name = StringField('name')

u = User(id=1, pwd='13544324', name='wjc')
u.save()
print_line()

#枚举类 from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6

w1 = Weekday.Sun
print(w1)
print_line()

#__iter__
class Fib(object):
    def __init__(self, n):
        self.__a = 0
        self.__b = 1
        self.__n = n
    def __iter__(self):
        return  self
    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__n > 0:
            self.__n -= 1
            if self.__n == 0:
                raise StopIteration()
        return self.__a

for k in Fib(10):
    print(k)
print_line()

#__getitem__
class Fib(object):
    def __getitem__(self, n):
        a = 0
        b = 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#如果参数是切片
            start = n.start
            end = n.stop
            L = []
            if start == None:#未提供start,从0开始
                start = 0
            if end == None:#未提供end,返回空
                return L
            for x in range(end):
                a, b = b, a + b
                if x >= start:
                    L.append(a)
            return L

print(Fib()[10])
print(Fib()[1:3])
print(Fib()[:5])
print_line()

#__getattr__
class Chain(object):
    def __init__(self, path=''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('{0}/{1}'.format(self.__path, path))
    def __str__(self):
        return self.__path
    __repr__ = __str__  #__str__ 返回可打印信息:>>>Chain()
                        #__repr__返回实例的信息:print(Chain())

print(Chain().home.wangjiangchuan.BlueTooth.Suntec)
print(Chain().usr.bin.bluetooth)
print_line()

#__call__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is {0}.'.format(self.name))
    def __str__(self):
        return self.name

s = Student('Mike')
s()
print_line()

