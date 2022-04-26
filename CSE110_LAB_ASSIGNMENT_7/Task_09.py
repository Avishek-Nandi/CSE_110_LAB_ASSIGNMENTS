# Solution to task 9

def distance(tup):
    dist = ((tup[0]) ** 2 + (tup[1]) ** 2) ** (1 / 2)
    return dist


def min_dist(given_list):
    for i in range(len(given_list)):
        for j in range(len(given_list) - i - 1):
            if distance(given_list[j]) > distance(given_list[j + 1]):
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]

    return f"Minimum distance = {distance(given_list[0])} Here the closest point is {given_list[0]}" \
           f" which has a distance of {distance(given_list[0])} from the origin."


if __name__ == '__main__':
    points = [(5, 3), (2, 9), (-2, 7), (-3, -4), (0, 6), (7, -2)]  # Sample Input  1
    print(min_dist(points))
