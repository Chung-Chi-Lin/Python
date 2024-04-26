# Python 中的 for 迴圈
# 指定次數

# in 後方皆可以疊代的數據
for x in range(-1):
    print(x)

# range(起始, 結束, 累加值)
for x in reversed(range(1, 12, 4)):
    print(x)

# items()
my_dict = {"a": 1, "b": 2, "c": 3}
for value in my_dict.items():
    print("value", value)
