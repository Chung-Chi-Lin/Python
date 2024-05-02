# Python 的邏輯運算子

# and
temp = int(input('請輸入現在溫度'))
if temp >= 20 and temp <= 25:
    print('現在的溫度適合生存')
elif temp >= 30 or temp <= 0:
    print('現在的溫度不適合生存')
else:
    print('請配戴生存工具')