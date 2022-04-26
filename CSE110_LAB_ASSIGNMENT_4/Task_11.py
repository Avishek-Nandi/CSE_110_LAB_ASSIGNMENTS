# Solution to task 11

user_input = input("Sir, please enter your desired list: ")
user_input = user_input[1:len(user_input)-1]

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

user_input1 = input("Sir, please enter your desired list: ")
user_input1 = user_input1[1:len(user_input1)-1]

list_of_str1 = user_input1.split(",")
list_of_numbers1 = []

for number in list_of_str1:
    list_of_numbers1.append(int(number.strip()))

common = False

for item in list_of_numbers:
    if item in list_of_numbers1:
        common = True

print(common)