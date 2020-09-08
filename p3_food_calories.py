#         Foods and Calories
#
# You visit a resutrant called Moms_cafe and food items in this resturant are sorted based on the amount of calories.
# you have to reverse this list of food items and their calories.
# 1 --> Inbuilt method
# 2 --> listname [::-1] slicing trick
# 3 --> swapping first element with last one ans second element with second last one and so on.
#
# Input :
#         Take a list as input from user
#     [1,4,5,9]
# Output :
#     [9,5,4,1]
#
# Alll the three methods give same results

# method 1
food = input("Enter food items in increasing order of kalories:").split(",")
print(list(reversed(food)))
# using slicing
print(food[::-1])
# using swaping
a, b = 0, 0
length = len(food)
for i in range(len(food) // 2):
    a = food[i]
    b = food[-i - 1]
    food[i] = b
    food[-i - 1] = a
print(food)
