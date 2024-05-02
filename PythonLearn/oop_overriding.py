# 子類別重寫父類別方法

class Animal:
    def eat(self):
        print("動物正在吃東西")

class Mammel(Animal):
    def hi(self):
        print("我是哺乳類")
    pass


class Rabbit(Mammel):
    def eat(self):
        print("兔子在吃紅蘿蔔")

animal = Animal()
animal.eat()

rabbit = Rabbit()
rabbit.eat()