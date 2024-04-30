# 可以查找 對應方法使用 help(random)
import random

# randint() 區間的整數
print(random.randint(1,10))

# random() 0~1的浮點數
print(random.random())

# 列表中隨機選擇一個元素
options = ["剪刀", "石頭", "布"]
rand_option = random.choice(options)
print(rand_option)

# 將列表打亂
cards = ["2", "3", "4", "5", "6"]
random.shuffle(cards)
print(cards)

# 猜數字遊戲
current_num = 0
def randint_num():
    global current_num
    current_num = random.randint(1, 100)

while True:
    try:
        input_num = int(input("結束請輸入q，請輸入要猜的數字:"))
        if input_num == "q":
            break
        if input_num == current_num:
            print("猜對拉!")
            randint_num()
            print("已重置數字!")
        elif input_num < current_num:
            print(f"還沒猜對給你提示，比{input_num}大")
        elif input_num > current_num:
            print(f"還沒猜對給你提示，比{input_num}小")
        elif input_num > 100 or input_num < 0:
            print("請輸入1~100數字")
    except ValueError:
        print("僅能輸入數字，請輸入1~100數字")