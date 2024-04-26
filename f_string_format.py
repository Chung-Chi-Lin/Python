# f-string 字串格式化

price_1 = 3.1415
price_2 = -77
price_3 =15.11

# 小數點精確度
print(f"價格 1 為 {price_1:.2f}\n"
      f"價格 2 為 {price_2:.2f}\n"
      f"價格 3 為 {price_3:.2f}")
# 加上正號或負號
print(f"價格 1 為 {price_1:+.2f}\n"
      f"價格 2 為 {price_2:+.2f}\n"
      f"價格 3 為 {price_3:+.2f}")

# 對齊 > < ^
print(f"價格 1 為 {price_1:>10.2f}\n"
      f"價格 2 為 {price_2:>10.2f}\n"
      f"價格 3 為 {price_3:>10.2f}")

# 混合符號
print(f"價格 1 為 {price_1:^+.2f}\n"
      f"價格 2 為 {price_2:^+.2f}\n"
      f"價格 3 為 {price_3:^+.2f}")