# if else elif 控制流程

# Boolean 布林值
for_sale = True
if for_sale:
    print("此項目正在出售")
else:
    print("此項目未出售")
# if else
age = 28
if age >= 20:
    print("年齡已滿20歲")
else:
    print("年齡尚未滿20歲")
# elif => else if 縮寫
while True:
    try:
        account_age = int(input("請輸入你的年齡"))
        break
    except ValueError:
        print("請輸入整數")

if account_age >= 100:
    print("你超過100歲無法註冊")
elif account_age > 18:
    print("年滿18歲可以註冊")
elif account_age < 0:
    print("出生了再來註冊")
else:
    print("你尚未滿18歲，不能註冊")
# 練習
