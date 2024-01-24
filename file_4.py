# This Program by m.mahadi program number 4
# roots of quadratic equation
import math


def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d <= 0:
        print('Root is not defined')
    else:
        X1 = -b + math.sqrt(b ** 2 - 4 * a * c) / 2 * a
        X2 = -b + math.sqrt(b ** 2 - 4 * a * c) / 2 * a
        print(f'X1={X1}\nX2={X2}')


a, b, c = map(float, input().split())
quadratic(a, b, c)



