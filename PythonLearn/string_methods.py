# Python 的字串方法

# `len()`、`find()`、`capitalize()`、
# `upper()`、`lower()`、`count()` 和 `replace()`

# help(str)

# 使用者的全名
name = "codePython77"

# 幾個字元
length = len(name)
print("您的全名有:", length, "個字元。")

# 找到第一個空格
space_pos = name.find("7")
print("第一個 7 出現在第:", space_pos, "個字元。")

# 首字母大寫
name_capitalize = name.capitalize()
print("第一個字母變成大寫:", name_capitalize)

# 所有字母變成大寫
name_upper = name.upper()
print("所有字母大寫:", name_upper)

# 所有字母變為小寫
name_lower = name.lower()
print("所有字母變為小寫:", name_lower)

# 計算所有指定字串有幾個
name_count = name.count("o")
print("計算字母 o 在字串中有幾個:", name_count)

# 替換指定字串
name_replace = name.replace("77", "Iam77")
print("替換 77 字串:", name_replace)
age = 18

# 程式練習: 驗證使用者輸入的合法性
# - 使用者名稱不能超過 12 字元、不能包含空格、不能包含數字
# - 如果都符合顯示 歡迎 + 使用者輸入文字
name = input("請輸入名稱:")
if len(name) > 12:
    print("使用者名稱不能超過 12 字元")
elif " " in name:
    print("不能包含空格")
elif not name.isalpha():
    print("不能包含其他字元")
else:
    print(f"歡迎{name}")