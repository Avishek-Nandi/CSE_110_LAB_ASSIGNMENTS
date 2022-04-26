# Solution to task 11

given_string = input("Enter a text:")
given_string = given_string.strip("{} ")
given_string = given_string.lower()
given_string = given_string.replace(" ", "")
output_dict = {}
freq = 0

for count in given_string:
    if count in output_dict:
        output_dict[count] = output_dict[count] + 1
    else:
        output_dict[count] = 1

print(output_dict)
