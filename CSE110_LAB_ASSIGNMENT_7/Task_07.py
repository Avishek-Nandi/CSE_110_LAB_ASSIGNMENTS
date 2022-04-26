# Solution to task 7

def conversion(str_list):
    temp = str_list[1:len(str_list)-1:]
    result_list = temp.split(',')
    result_list = [int(k) for k in result_list]
    return result_list


list_1 = conversion(input("Enter 1st list: "))
list_2 = conversion(input("Enter 2nd list: "))
list_1.extend(list_2)

list_1.sort()
print("Sorted list=", list_1)

if len(list_1) % 2 != 0:
    print("Median=", list_1[int(len(list_1)/2)])
else:
    print("Median=", (list_1[int(len(list_1)/2)]+list_1[int(len(list_1)/2)-1])/2)
