# Solution to Task 10

def make_square(start, limit):
    global dic
    if start == limit:
        dic[limit] = limit ** 2
        print(dic)
        return
    else:
        dic[start] = start ** 2
        make_square(start+1, limit)


if __name__ == '__main__':
    dic = {}
    make_square(1, 3)

# # Solution to Task 10 Aproach 2
#
# def make_square(start, limit):
#     global dic
#     for i in range(start, limit+1):
#         dic[i] = i**2
#     print(dic)
#
#
# dic = {}
# make_square(5, 9)
