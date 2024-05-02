class Car:
    wheel = 4
    def __init__(self, make, model, year, color):
        # 初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car("Ford", "Honda", 2023, "藍色")

print(car1.wheel)

car2 = Car("三葉", "勁戰", 2016, "白色")

car2.wheel = 2
print(car2.wheel)
