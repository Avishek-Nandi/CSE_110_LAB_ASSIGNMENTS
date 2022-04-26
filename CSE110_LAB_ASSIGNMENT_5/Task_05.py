# Solution to Task 5

given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

user_input = int(input("Sir, please enter your desired number: "))

instances = 0

for i in given_tuple:
    if i == user_input:
        instances += 1

print(f"{user_input} appears {instances} times in the tuple")
