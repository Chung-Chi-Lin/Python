# Python 中的方法鏈 Method Chaining

class Car:
    def turn_on(self):
        print("你啟動了引擎")

        return self
    def drive(self):
        print("你開車了")

        return self
    def stop(self):
        print("你踩了煞車")
        return self

    def turn_off(self):
        print("你關閉了引擎")
        return self

car = Car()
car.turn_on().drive().stop().turn_off()