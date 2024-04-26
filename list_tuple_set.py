# Python 中的集合 list, sets 與 tuple

# list 列表
fruits = ['apple', 'banana', 'watermelon']

fruits.append('orange')
fruits.index('banana')
fruits.remove('watermelon')
fruits.count('watermelon')

# set 集合
cars_set = {'benz', 'toyota', 'mazda'}

cars_set.add('gtr')
for car in cars_set:
    print(car, end=" ")

if 'gtr' in cars_set:
    print("You hava gtr!")

# tuple 元組可以試用()包覆或不包覆
animals = ('dog', 'cat', 'elephant', 'dog')

print(animals.count('dog'))