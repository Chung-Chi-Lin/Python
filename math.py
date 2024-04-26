# Python 中的數學
# 加減乘除
apples = 3
apples += 2
print(apples)

apples -= 2
print(apples)

apples *= 5
print(apples)

apples /= 5
print(int(apples))

# 指數 (平方, 三次方)
banana = 3
banana **= 2
print(int(banana))

# 模數 mod
# 10 mod 3 等於 3 餘 1
print(10 % 3)
# 11 mod 3 等於 3 餘 2
print(11 % 3)
# 12 mod 3 等於 4 餘 0
print(12 % 3)

# 內置數學函數

# 次方 pow
print(pow(3,2))

# 最大值 Max 與最小值 Min
x = 1
y = 2
z = 3
print(max(x, y, z))
print(min(x, y, z))

# 四捨五入 round
a = 3.14
print(round(a))
b = 3.5
print(round(b))

#絕對值
c = -4
print("絕對值", abs(c))