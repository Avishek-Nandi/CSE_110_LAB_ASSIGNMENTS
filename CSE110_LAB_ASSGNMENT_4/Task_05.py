# Solution to task 5

user_input = input("Sir, please enter your desired list: ")
user_input = user_input[1:len(user_input)-1]

list_of_str = user_input.split(",")
list_of_words = []
for number in list_of_str:
    list_of_words.append(number.strip('" '))

result = []

for values in list_of_words:
    if values != '':
        result.append(values)

print("Original List: ",list_of_words)
print("Modified List: ",result)
