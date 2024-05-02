# args => arguments 任意數量的參數 * => tuple
# kwargs => 關鍵字 + args (keyword args) ** => dictionary

# args

def add(a, b):
    return a + b
print(add(1,2))

# 一個 * 字號
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3))

# 二個 * 字號
def print_info(**kwargs):
    for index, value in kwargs.items():
        print(f"{index}參數, 值為{value}")

print_info(name="小明", age= 15, isMale=True)
