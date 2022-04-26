# Solution to task 6

def sort(list2):
    list1 = list2.copy()
    count = 0

    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    for m in range(len(list1)):
        if list1[m] != list2[m]:
            count = count+1

    return count


my_list = [4, 2, 3, 1, 6, 5]
print("Times position changed:", sort(my_list))

