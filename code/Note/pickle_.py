import pprint, pickle

def print_line(n = 30):
    print("=" * n)

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('1.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

pk_file = open("1.pkl", "rb")

data = pickle.load(pk_file)
pprint.pprint(data)

data2 = pickle.load(pk_file)
pprint.pprint(data2)

pk_file.close()
print_line()
#dumps, loads, dumps, loads
p1 = pickle.dumps(data1)
print(p1)
p2 = pickle.loads(p1)
print(p2)
p2 = pickle.dumps(data1, True)
print(p2)
p3= pickle.loads(p2)
print(p3)
print_line()
#dump, dump, dump, load, load, load
a1 = 'apple'
b1 = {1: 'One', 2: 'Two', 3: 'Three'}
c1 = ['fee', 'fie', 'foe', 'fum']

file1 = open('1.pkl', 'wb')
pickle.dump(a1, file1, True)
pickle.dump(b1, file1, True)
pickle.dump(c1, file1, True)
file1.close()

file2 = open('1.pkl', 'rb')
a2 = pickle.load(file2)
print(a2)
b2 = pickle.load(file2)
print(b2)
c2 = pickle.load(file2)
print(c2)
print_line()
#查看当前版本，查看当前版本之前的历史版本
print(pickle.format_version)
print(pickle.compatible_formats)
print_line()
#对象引用的维护
a = [1, 2, 3]
a.append(4)
b = a
p1 = pickle.dumps((a, b))
d, e = pickle.loads(p1)
d.append(5)
print(a, b, d, e)
print_line()
#递归引用
l = [1, 2, 3]
l.append(l)
print('l: {0}'.format(l))
print('l[3]: {0}'.format(l[3]))
print('l[3][3]: {0}'.format(l[3][3]))
p1 = pickle.dumps(l)
l2 = pickle.loads(p1)
print('l2: {0}'.format(l2))
print('l2[3]: {0}'.format(l2[3]))
print('l2[3][3]: {0}'.format(l2[3][3]))
print_line()
#循环引用
a = [1, 2]
b = [3, 4]
a.append(b)
b.append(a)
print('a: {0}'.format(a))
print('b: {0}'.format(b))
print('a[2]: {0}'.format(a[2]))
print('b[2]: {0}'.format(b[2]))
file = open('1.pkl', 'wb')
p1 = pickle.dump((a, b), file)#元组pickle
file.close()
file2 = open('1.pkl', 'rb')
c, d = pickle.load(file2)
file2.close()
print('c: {0}'.format(c))
print('d: {0}'.format(d))
print(a is c)#load获得对象为dump的副本
print(b is d)
file = open('1.pkl', 'wb')
pickler = pickle.Pickler(file)#Pickler
pickler.dump(a)
pickler.dump(b)
file.close()
file = open('1.pkl', 'rb')
unpickler = pickle.Unpickler(file)
c = unpickler.load()
d = unpickler.load()
print(a is c)
print(b is d)
print_line()
#文件对象不可pickle
# file = open('1.pkl', 'w')
# p1 = pickle.dump(file)
# file.close()

#对类实例进行pickle
#pickle:调用__getstate__
#unpickle:调用__setstate__
class Foo(object):
    def __init__(self, value, filename):
        self.value = value
        self.logfile = open(filename, 'w')
    def __getstate__(self):
        """Return state values to be pickled."""
        f = self.logfile
        return (self.value, f.name, f.tell())
    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        self.value, name, position = state
        f = open(name, 'w')
        f.seek(position)
        self.logfile = f

#对类实例进行pickle
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __getstate__(self):
        # pickle的是对象属性名与值的字典
        return {'firstname': self.firstname, 'lastname': self.lastname}
    def __setstate__(self, state):
        if 'firstname' in state:
            self.firstname = state['firstname']
        if 'lastname' in state:
            self.lastname = state['lastname']
    def __str__(self):
        return "firstname: " + self.firstname + " lastname: " + self.lastname

file = open('1.pkl', 'wb')
person = Person('w', 'jc')
print('before pickle: {0}'.format(person))
p = pickle.dump(person, file)
file.close()

#对上面已pickle的Person实例unpickle并修改属性
class Person(object):
    def __init__(self, fullname):
        self.fullname = fullname
    def __setstate__(self, state):
        if 'fullname' not in state:
            first = ''
            last = ''
            if 'firstname' in state:
                first = state['firstname']
                del state['firstname']#删除firstname
            if 'lastname' in state:
                last = state['lastname']
                del state['lastname']#删除lastname
            self.fullname = ' '.join((first, last)).strip()#添加fullname属性
        self.__dict__.update(state)
    def __str__(self):
        return "fullname: " + self.fullname

file = open('1.pkl', 'rb')
person = pickle.load(file)
print('after unpickle: {0}'.format(person))
file.close()
print_line()