# Python 中的 while 迴圈

name = input("請輸入你的名字")
while name != "q":
    print(f"你輸入的是{name}")
    name = input("請輸入你的名字")
print("你已經離開迴圈")

# 優化
while True:
    name = input("請輸入你的名字")
    if name == "q":
        break
    print(f"你輸入的名字是{name}")
print("你已經離開迴圈")

# 進階用法
import random
current_num = random.randint(1,10)

while True:
    try:
        num = int(input("終極密碼1~10"))
        if 1 <= num <= 10:
            if num == current_num:
                print("BOOM!")
                break
            else:
                print("你沒有猜中ㄏㄏ")
        else:
            print("請選擇1~10的數字")
    except ValueError:
        print("輸入數字1~10區間")