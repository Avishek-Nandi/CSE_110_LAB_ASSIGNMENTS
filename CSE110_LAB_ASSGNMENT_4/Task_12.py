# Solution to task 12

user_input = input("Sir, please enter your desired list: ")

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

largest = list_of_numbers[0]
second_largest = "n/a"
largest_index = 0
second_largest_index = "n/a"

for position in range(1, len(list_of_numbers)):

    if list_of_numbers[position] > largest:
        second_largest = largest
        second_largest_index = largest_index
        largest = list_of_numbers[position]
        largest_index = position
    elif second_largest == "n/a" or list_of_numbers[position] > second_largest:
        second_largest = list_of_numbers[position]
        second_largest_index = position


print("My list:", list_of_numbers)
print("Second largest number in the list is", second_largest, "which was found at index", second_largest_index)
