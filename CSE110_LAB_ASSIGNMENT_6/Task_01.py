# Solution to the task 1

def even_checker(number):
    print('Even!!') if number % 2 == 0 else print('Odd!!')   # shorthand


if __name__ == '__main__':
    user_input = input('Sir, Please enter your desired number: ')
    even_checker(user_input)
