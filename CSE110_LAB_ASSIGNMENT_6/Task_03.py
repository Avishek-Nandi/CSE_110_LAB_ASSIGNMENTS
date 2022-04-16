# Solution to the task 3

def foo_moo(number):
    a = number % 2 == 0
    b = number % 3 == 0
    print('Foomoo') if a and b else print('Foo') if a else print('Moo') if b else print('Boo')


if __name__ == '__main__':
    user_input = int(input("Sir, Enter your desired number: "))
    foo_moo(user_input)
