# Solution to task 9

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Pierre Cox': 190}

output_dict = {}
user_input = int(input("Enter a number: "))

for keys, values in exam_marks.items():
    if values >= user_input:
        output_dict[keys] = values

print("Output is", output_dict)
