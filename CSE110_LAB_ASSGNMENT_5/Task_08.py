# Solution to task 8

input_str = input("Enter the input:")
temp_str = input_str.replace("'", "")
temp_str = temp_str[1:len(temp_str)-1:]
final_str = temp_str.split(",")
sample = {}

for count in final_str:
    keyval = count.split(":")
    sample[keyval[0]] = int(keyval[1])

total_val = 0
temp = 0

for keys, values in sample.items():
    total_val = total_val+values
    temp = temp+1

print("Average is", total_val/temp)
