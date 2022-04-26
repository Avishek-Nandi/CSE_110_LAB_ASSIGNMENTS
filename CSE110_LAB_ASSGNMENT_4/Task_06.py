# Solution to task 6

user_input = input("Sir, please enter your desired string of 7 numbers separated by commas: ")
user_input = user_input[1:len(user_input)-1]

list_of_str = user_input.split(",")
list_of_numbers = []

for number in list_of_str:
    list_of_numbers.append(int(number.strip()))

largest = list_of_numbers[0]
index = 0

for position in range(1, len(list_of_numbers)):
    if list_of_numbers[position] > largest:
        largest = list_of_numbers[position]
        index = position

print("My list:", list_of_numbers)
print("Largest number in the list is", largest, "which was found at", index)
