# Solution to Task 12

def function_name(given_list):
    result = []
    removed = 0
    for i in given_list:
        if result.count(i) < 2:
            result.append(i)
        else:
            removed += 1
    print(f"Removed: {removed}\n{result}")


function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])
