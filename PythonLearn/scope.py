# Python 中的作用域
# LEGB 作用域順序

# L - local 區域
# E - enclosed
# G - Global 全域
# B - built-in

# 變數範圍

a = 10
def function_one():
    a = 1
    print("a", a)
    def function_two():
        b = 2
        print("b:", b)
        print("a:", a)
    function_two()
function_one()

# 修改外層變數 global
def change_a(val):
    global a
    a = val

change_a(20)
print(a)

# built-in
from math import e
print(e)

def function_one():
    print(e)