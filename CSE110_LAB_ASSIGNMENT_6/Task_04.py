# Solution to the task 4

def function_name(string):

    upper_case = 0
    lower_case = 0

    for char in string:
        if ord('A') <= ord(char) <= ord('Z'):
            upper_case += 1
        elif ord('a') <= ord(char) <= ord('z'):
            lower_case += 1

    print("No. of Uppercase characters :", upper_case)
    print("No. of Lowercase Characters :", lower_case)


if __name__ == '__main__':
    user = input("Sir, please enter your desired text: ")
    function_name(user)
