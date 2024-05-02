# Python 中的異常處理 try except

# exception

try:
    x = int(input("請輸入第一個整輸"))
    y = int(input("請輸入第二個整輸"))
    print(x/y)
except (ValueError, ZeroDivisionError):
    print("出現錯誤重新輸入")
else:
    print("除了except上的，其他錯誤會跑這段")
finally:
    print("無論是否出現異常，都會執行")
