# Solution to task 3

def inverse_selection_sort(my_list):
    for i in range(len(my_list)):
        max_index = i
        for j in range(i, len(my_list)):
            if my_list[max_index] < my_list[j]:
                max_index = j

        my_list[i], my_list[max_index] = my_list[max_index], my_list[i]

    return my_list


my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
print("Descending ordered list:", inverse_selection_sort(my_list))