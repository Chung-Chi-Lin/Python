# 購物車程式

# list, set, tuple
products = []
prices = []

# 無窮迴圈(記得設置 break)
while True:
    product = input("請輸入想購買的物品:")
    if product.lower() == "q":
        break

    price = float(input(f"請輸入 {product} 的價格:"))
    products.append(product)
    prices.append(price)

print("商品", products)
print("價格", prices)

# enumerate 列出列表索引與參數

for index, product in enumerate(products):
    print(f"第{index+1} 個商品為 {product}, 價格為{int(prices[index])}")