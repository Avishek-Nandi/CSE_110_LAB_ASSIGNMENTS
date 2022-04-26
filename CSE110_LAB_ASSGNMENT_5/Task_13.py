# Solution to task 13

given_list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
output_dict = {}

for i in given_list:
    output_dict[i[0]] = []

for j in given_list:
    for keys, values in output_dict.items():
        if keys == j[0]:
            output_dict[keys].append(j[1])

print("Output is: ", output_dict)
