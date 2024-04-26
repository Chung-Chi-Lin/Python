# 巢狀迴圈
row = int(input("請輸入行數:"))
cols = int(input("請輸入列數:"))
symbol = input("請輸入符號:")

# print 第二個參數 end 代表結尾，預設為換行
for i in range(row):
    for j in range(cols):
        print(symbol, end=" ")
    print()