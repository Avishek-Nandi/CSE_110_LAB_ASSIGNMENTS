# Solution to Task 13

def input_taker():
    try:
        operator = input("Sir, which function do you want to use? (+, -, *, /) :")
        num = float(input("Enter first number: "))
        num1 = float(input("Enter second number: "))
        print(function_name(operator, num, num1))
    except:
        print('============================================')
        print('Invalid Input Please try again')
        input_taker()


def function_name(operator, num, num1):

    if operator == '+':
        return num + num1
    elif operator == '-':
        return num - num1
    elif operator == '*':
        return num * num1
    elif operator == '/':
        return num / num1
    else:
        print('============================================')
        print('Invalid Input Please try again')
        input_taker()


if __name__ == '__main__':
    input_taker()
