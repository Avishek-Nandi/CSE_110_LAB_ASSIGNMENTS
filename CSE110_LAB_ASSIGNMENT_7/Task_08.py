# Solution to task 8

str_list = input("Enter a list: ")
temp = str_list[1:len(str_list)-1:]
list_one = temp.split(',')
list_one = [int(k) for k in list_one]

minimum = abs(list_one[0]+list_one[1])
minimum_pos = 0
minimum_neg = 1

for i in range(len(list_one)-1):
    for j in range(i+1, len(list_one)):
        if abs(list_one[i] + list_one[j]) < minimum:
            minimum = abs(list_one[i]+list_one[j])
            minimum_pos = list_one[i]
            minimum_neg = list_one[j]
print("Two pairs which have the smallest sum =", minimum_pos, "and", minimum_neg)
