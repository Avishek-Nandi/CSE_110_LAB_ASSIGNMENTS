# Solution to task 13

user_input = input("Sir, please enter your desired list: ")

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

largest = list_of_numbers[0]
smallest = list_of_numbers[0]
largest_index = 0
smallest_index = 0

for position in range(1, len(list_of_numbers)):

    if list_of_numbers[position] > largest:
        largest = list_of_numbers[position]
        largest_index = position
    elif list_of_numbers[position] < smallest:
        smallest = list_of_numbers[position]
        smallest_index = position

print("My list:", list_of_numbers)
print("Smallest number in the list is", smallest, "which was found at", smallest_index)
print("Largest number in the list is", largest, "which was found at", largest_index)

