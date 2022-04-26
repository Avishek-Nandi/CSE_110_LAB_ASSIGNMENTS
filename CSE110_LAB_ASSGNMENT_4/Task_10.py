# Solution to task 10

user_input = input("Sir please enter your desired list: ")

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

result_list = []

for item in list_of_numbers:
    if item not in result_list:
        result_list.append(item)

print(f"Input list: {list_of_numbers}")
print(f"Modified list: {result_list}")
