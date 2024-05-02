# 獠牙運算符 :=

# foods = []
#
# while True:
#     food = input("你喜歡什麼食物?")
#     if food == "quit":
#         break
#     foods.append(food)
#
# print(foods)

# 簡化

foods = []

while (food := input("你喜歡什麼食物?")) != "quit":
    # if food == "quit":
    #     break
    foods.append(food)

print(foods)
