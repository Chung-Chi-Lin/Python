# Python 字典入門

# 鍵 => 值
# Key => Value

capital = {
    "United States": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris",
    "Russia": "Moscow"
}

# get() 取得鍵值對
print(capital.get("France"))

# update() 更新鍵值對
capital.update({"Germany": "Berlin"})
print(capital)

# pop() 刪除鍵值對
capital.pop("United States")
print(capital)

# values() 獲得所有值
print(capital.values())

# items() 獲得所有鍵值對
print(capital.items())