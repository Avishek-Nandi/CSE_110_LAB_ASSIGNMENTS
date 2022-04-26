# Solution to Task 2

user_input = input("Sir, please enter your desired tuple: ")[1:-1]

user_list = user_input.split(", ")
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

result_tuple = tuple(user_list[2:len(user_list) - 2])

print(result_tuple)
