# Solution to the task 7

def show_palindrome(number, i=1):
    if number == i:
        print(number, end="")
        return
    else:
        print(i, end="")
        show_palindrome(number, i+1)
        print(i, end="")


if __name__ == '__main__':
    user = int(input("Sir, please enter your desired number: "))
    show_palindrome(user)
