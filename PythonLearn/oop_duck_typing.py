class Duck:
    def walk(self):
        print("鴨子在走路")
    def talk(self):
        print("鴨子在呱呱呱")

class Chicken:
    def walk(self):
        print("雞在走路")
    def talk(self):
        print("雞在咕咕叫")

# 即使沒有繼承的關係，也可當作同一類型的類別使用

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()

duck = Duck()
chicken = Chicken()

person = Person()
person.catch(duck)