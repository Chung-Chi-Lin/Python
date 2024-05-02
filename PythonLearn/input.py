# input 取得使用者輸入
name = input("請輸入你的名字:")
print(f"你得名字是{name}")
# 練習一: 填詞遊戲
adj_1 = input("請輸入心情形容詞")
print(f"我今天很{adj_1}")
adj_2 = f"我今天很{adj_1}"
adj_3 = input("請輸入名詞")
print(f"{adj_2}，我想要吃{adj_3}")
# 練習二: 計算面積
num_1 = float(input("請輸入長度"))
num_2 = float(input("請輸入寬度"))
print(f"總面積為:{num_1 * num_2}")
# 練習三: 購物
product_1 = input("請輸入商品名稱")
while True:
    try:
        product_2 = int(input("請輸入商品數量"))
        break
    except ValueError:
        print("輸入錯誤! 請輸入整數。")
product_3 = int(input("請輸入商品價格"))
total_cost = product_2 * product_3
print(f"今天我買了{product_1}，我買了{product_2}個，一個是{product_3}元，總共花了我{total_cost}元")