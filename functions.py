# function(method)

# 函式 def 定義
def say_hello():
    print("Hello! World!")

say_hello()

# 傳遞參數
def greeting(name):
    print(f"你好, {name}")

greeting("77")

# 函式的預設引數 (default arguments)
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

greet("77")
# 關鍵字引數，指定參數
greet(greeting="你好", name="小明")

def default_test(name="77", greeting="你好"):
    print(f"{greeting} {name}")
default_test()