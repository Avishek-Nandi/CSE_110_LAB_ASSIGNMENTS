# Solution to task 2

user_input = input("Sir, please enter your desired list: ")
user_input = user_input[1:len(user_input)-1]

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

result = list_of_numbers[2:len(list_of_numbers)-2]

if len(list_of_numbers) > 3:
    print(result)
else:
    print("Not possible")
