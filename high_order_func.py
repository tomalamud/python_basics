# What a high order function really is:
def saludo(func):
    func()

def hola():
    print('Hola!')

def chau():
    print('Chau!')

saludo(hola)
saludo(chau)

# The most important ones:
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

# FILTER
# it can be done with list comprehensions...
fcomprehensions = [i for i in my_list if i % 2 != 0]
print(fcomprehensions)
# but, the cooler way is with filter()
filterhensions = list(filter(lambda x: x % 2 != 0, my_list))
print(filterhensions)

# MAP
mcomprehensions = [i**2 for i in my_list]
print(mcomprehensions)
maprehensions = list(map(lambda x: x**2, my_list))
print(maprehensions)

# REDUCE
# with for
all_multiplied = 1
for i in my_list:
    all_multiplied = all_multiplied * i
print(all_multiplied)
# with reduce
from functools import reduce
all_multiplied_reduce = reduce(lambda a, b: a * b, my_list)
print(all_multiplied_reduce)