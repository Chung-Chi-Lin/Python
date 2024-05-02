# OOP - Python 中的繼承

# 父類別 <-> 子類別

# 動物
class Animal:
    aLive = True

    def eat(self):
        print("這個動物在吃東西")

    def sleep(self):
        print("這個動物正在睡覺")

# 兔子
class Rabbit(Animal):
    def jump(self):
        print("這支兔子在跳")

# 繼承父類別方法
rabbit = Rabbit()
rabbit.jump()
rabbit.eat()