# Solution to task 4

user_input = input("Sir, please enter your desired list: ")
user_input = user_input[1:len(user_input)-1]

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

result_list = []

for values in list_of_numbers:
    if int(values) < 0:
        result_list.append((int(values)*-1)**2)
    else:
        result_list.append(int(values)**2)

print(result_list)
