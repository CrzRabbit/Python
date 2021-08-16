import random

print(random.random())

print(random.uniform(0, 10))

print(random.randrange(0, 10, 2))

print(random.choice(range(0, 10, 2)))

print(random.choice(['wang', 'jiang', 'chuan']))

list = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(list)
print(list)

print(random.sample(list, 2))