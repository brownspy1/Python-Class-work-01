# This Program by m.mahadi program number 2
# Area of a triangle

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(area)

a, b, c = list(map(float, input().split()))

if a + b <= c or a + c <= b or b + c <= a:
    print('It is not a valid triangle')
else:
    triangle_area(a, b, c)

