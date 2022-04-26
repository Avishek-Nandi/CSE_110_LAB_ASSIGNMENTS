# Solution to Task 6

decision = input('''Sir, which example would you like to test?
                 \nEnter 1 for Example 1\nEnter 2 for Example 2\n\n''')

if decision == 1:
    given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
else:
    given_tuple = (10, 20, 30, 40, 50, 60)

temp_list = list(given_tuple)
output_tuple = tuple(temp_list[::-1])
print()
print(output_tuple)
