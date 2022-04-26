# Solution to task 10

given = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure': 9}
temp = ""

maximum = 0  # Quantity can't be negative
max_key = None

for keys, values in given.items():
    if maximum < values:
        maximum = values
        max_key = keys

print("The highest selling book genre is", max_key, "and the number of books sold are", given[max_key])

