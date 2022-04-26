# Solution to task 5

def list_creator(user):
    list_user = user.strip("[] ").replace(" ", "").replace('"', '').split("],")
    for i in range(len(list_user)):
        list_user[i] = list_user[i].replace("[", "").split(",")
        for j in range(len(list_user[i])):
            try:
                list_user[i][j] = int(list_user[i][j])
            except:
                list_user[i][j] = list_user[i][j]
    list_adder(list_user)
    return list_user


def list_adder(list_user):
    global list_of_names, list_of_CSE110, list_of_PHY111, list_of_MAT110
    for name, cse, phy, mat in list_user:
        list_of_names.append(name)
        list_of_CSE110.append(cse)
        list_of_PHY111.append(phy)
        list_of_MAT110.append(mat)


def bubble_sort(user_list, list_of_names):
    for i in range(len(user_list)):
        for j in range(len(user_list) - i - 1):
            if user_list[j] < user_list[j + 1]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
                list_of_names[j], list_of_names[j + 1] = list_of_names[j + 1], list_of_names[j]
    return list_of_names


if __name__ == '__main__':
    user = '[ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]'
    list_of_names, list_of_CSE110, list_of_PHY111, list_of_MAT110 = [], [], [], []

    list_user = list_creator(user)
    print(list_creator(user))
    list_adder(list_user)

    des = input("Enter course: ").lower()

    print(bubble_sort(list_of_CSE110, list_of_names)) if des == "cse110" else print(
        bubble_sort(list_of_PHY111, list_of_names)) if des == "phy111" else print(
        bubble_sort(list_of_MAT110, list_of_names)) if des == "mat110" else print("Invalid Course")
