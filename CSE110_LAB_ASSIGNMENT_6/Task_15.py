# Solution to Task 15

def input_taker():
    user = input('Sir, please enter your desired list: ').replace('"', '')
    user = user.replace(']', '').replace('[', '').replace(' ', '').split(",")
    location = input("Sir, please enter a location: ").lower()
    if location == '':
        print(function_name(user))
    else:
        print(function_name(user, location))


def function_name(user, location='dhanmondi'):
    menu = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = 30 if location == 'dhanmondi' else 70
    for item in user:
        total += menu[item]
    return total


if __name__ == '__main__':
    input_taker()
