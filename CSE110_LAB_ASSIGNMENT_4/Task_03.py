# Solution to task 3

list_of_numbers = []
for i in range(1, 6):
    number = int(input("Sir, please enter you desired number: "))
    list_of_numbers.append(number)

print("Input data:", list_of_numbers)
print("Printing values from the list in reverse order: ")

# printing without for loop
print(*list_of_numbers[::-1], sep="\n")


# printing with for loop (Please uncomment to check)

# for i in range(4, -1, -1):
#     print(list_of_numbers[i])
