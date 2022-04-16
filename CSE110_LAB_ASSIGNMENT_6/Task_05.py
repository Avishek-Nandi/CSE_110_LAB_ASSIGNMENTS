# Solution to the task 5

def calculate_tax(age, salary, designation):
    tax = salary*0.05 if salary <= 20000 else salary*0.1
    return 0 if age < 18 or designation == "president" or salary < 10000 else tax


if __name__ == '__main__':
    user = input("Enter as string:").strip(' ()').split(",")
    print(calculate_tax(int(user[0]), int(user[1]), user[2].strip(" '\"").lower()))