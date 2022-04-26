# Solution to task 4


def descending_sort(my_list):
    for i in range(len(my_list)):
        max_index = i
        for j in range(i, len(my_list)):
            if my_list[max_index] < my_list[j]:
                max_index = j

        my_list[i], my_list[max_index] = my_list[max_index], my_list[i]

    return my_list


def ascending_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


sitting_list = [10, 30, 20, 70, 11, 15, 22, 16, 58, 100, 12, 56, 70, 80]
even = []
odd = []
sorted_list = []

for i in range(len(sitting_list)):
    if i % 2 == 0:
        even.append(sitting_list[i])
    else:
        odd.append(sitting_list[i])

even = ascending_sort(even)
odd = descending_sort(odd)
if len(odd) > len(even):
    for j in range(len(odd)):
        sorted_list.append(even[j])
        sorted_list.append(odd[j])

else:
    for j in range(len(odd)):
        sorted_list.append(even[j])
        sorted_list.append(odd[j])

print("Sorted list: ", sorted_list)
