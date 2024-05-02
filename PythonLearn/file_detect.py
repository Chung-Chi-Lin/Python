# 使用Python 進行檔案偵測

import os

str = r"C:\Users\zhongqilin\Desktop\主要開發內容.txt"
print(str)

if os.path.exists(str):
    print("該路徑為檔案!")
elif os.path.isdir(str):
    print("該路徑為目錄")
elif os.path.isfile(str):
    print("該路徑為檔案")
else:
    print("other")

# 開啟檔案
with open(str) as file:
    print(file.read())