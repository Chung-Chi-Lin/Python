# Python 中的數學
import math

# 四捨五入、無條件進位、無條件捨去
x = 9.5
print(round(x))
print(math.ceil(x))
print(math.floor(x))

# 圓周率
print(math.pi)

# 計算圓的周長 2πR
radius = float(input("請輸入圓的半徑"))
c = round(2 * radius * math.pi)
print(f"圓的周長為{ c }")

# 計算圓的面積 πR2
area = round(pow(math.pi * radius, 2))
print(f"圓的面積為{ area }")

