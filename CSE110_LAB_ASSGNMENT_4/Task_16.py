# Solution to task 16

user_input = input("Sir please enter your desired list: ").strip('[] "')

list_of_numbers = user_input.split(",")

for item in range(0, len(list_of_numbers)):
    list_of_numbers[item] = int(list_of_numbers[item])

modified_list = []

for item in list_of_numbers:
    if item not in modified_list:
        modified_list.append(item)

print("Given numbers in list:", list_of_numbers)
print("List without any dupliacte values:", modified_list)
