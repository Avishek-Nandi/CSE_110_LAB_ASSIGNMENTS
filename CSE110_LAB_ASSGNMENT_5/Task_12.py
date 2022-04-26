# Solution to task 12

given_dict = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count = 0

for keys, values in given_dict.items():
    for temp in values:
        count = count + 1

print("The total number of items in a dictionary’s values: ", count)
