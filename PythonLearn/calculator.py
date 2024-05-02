# Python 計算機程式
vaild_operator = ['+', '-', '*', '/']
operator = input('請輸入+、-、*、/')
if operator not in vaild_operator:
    print('請輸入符合計算符號')
else:
    num1 = float(input('請輸入第一個數字:'))
    num2 = float(input('請輸入第二個數字:'))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 != 0:
            result = num1/num2
        else:
            print('除數不得為零')
            result = None

    if result is not None:
        print(f'計算結果是{int(result)}')