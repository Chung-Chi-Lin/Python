# 購物車程式

# list, set, tuple
products = []
prices = []

product = input("請輸入想買的產品:")
price = input(f"請輸入 { product }價格:")

products.append(product)
prices.append(price)

find_product = input("請輸入要查詢的產品")

if find_product in products:
    index = products.find(find_product)
    if :
    print(f"有找到您的商品,價格是{}")
else:
    print("沒有找到對應的商品")