# Solution to the task 2

def fibonacci(limit, n=0, n1=1, f=True):
    new = n + n1
    if f:
        print(n, n1, end=" ")
    if new < limit:
        print(new, end=" ")
        fibonacci(limit, n1, new, False)
    else:
        return


if __name__ == '__main__':
    user_input = int(input("Please enter the limit: "))
    fibonacci(user_input)
