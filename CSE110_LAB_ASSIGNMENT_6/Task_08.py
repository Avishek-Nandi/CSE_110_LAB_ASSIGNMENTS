# Solution to the task 8

def show_palindrome(number, i=1):
    if number == i:
        print(number, end=" ")
        return
    else:
        print(i, end=" ")
        show_palindrome(number, i+1)
        print(i, end=" ")


def show_palindromic_triangle(number, i=1):
    if number == i:
        show_palindrome(number)
        print()
        return
    else:
        print((((number-i)*2)-1)*" ", end=" ")
        show_palindrome(i)
        print()
        show_palindromic_triangle(number, i+1)


if __name__ == '__main__':
    user = int(input("Sir, please enter your desired number: "))
    show_palindromic_triangle(5)
