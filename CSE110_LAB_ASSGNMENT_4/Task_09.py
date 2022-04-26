# Solution to task 9

user_input = input("Sir please enter your desired list: ")

user_input += " "
list_of_numbers = []
char = ""

for i in user_input:
    if i == " ":
        list_of_numbers.append(int(char))
        char = ""
    else:
        char += i

print("Original list:",list_of_numbers)

list_of_numbers_result = []

for number in list_of_numbers:
    if number % 2 != 0:
        list_of_numbers_result.append(number)

print("Modified list:",list_of_numbers_result)