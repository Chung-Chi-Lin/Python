# Python 販賣機程式
menu = {
    "披薩": 300,
    "爆米花": 200,
    "薯條": 90,
    "可樂": 50,
    "雪碧": 50
}

cart = []
total = 0
print("menu>>")
for item, price in menu.items():
    print(f"{item}")

while True:
    food = input("請輸入要點餐的菜單項目")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")

print(f"總共: {total}元")