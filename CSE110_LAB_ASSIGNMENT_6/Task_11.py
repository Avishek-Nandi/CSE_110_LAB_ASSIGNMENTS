# Solution to Task 11

def rem_duplicate(given_tuple):
    result = []
    for i in given_tuple:
        if i not in result:
            result.append(i)
    print(tuple(result))


if __name__ == '__main__':
    rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))

