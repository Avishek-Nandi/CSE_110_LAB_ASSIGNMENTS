# Solution to the task 6

def function_name(days):
    print(days // 365, "years", end=", ")
    print((days % 365) // 30, "months", end=" and ")
    print((days % 365) % 30, "days")


if __name__ == '__main__':
    user = int(input("Sir please enter the amount of days: "))
    function_name(user)


