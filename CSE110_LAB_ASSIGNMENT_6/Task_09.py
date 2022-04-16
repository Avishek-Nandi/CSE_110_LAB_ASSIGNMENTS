# Solution to Task 9
from math import pi


def area_circumference_generator(radius):
    area = pi * radius * radius
    circumference = pi* 2 * radius
    return area, circumference


if __name__ == '__main__':
    user = int(input("Sir, please enter your desired radius: "))
    area, circumference = area_circumference_generator(user)
    print(f"Area of the circle is {area} and circumference is {circumference}")
