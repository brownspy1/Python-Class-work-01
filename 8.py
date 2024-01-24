# This Program by m.mahadi program number 8
# find bigast number in 3 numba (mathod 1)
def find_max(a, b, c):
    if a > b and a > c:
        print('A is Bigast')
    elif b>a and b>c:
        print('B is Bigast')
    elif c>a and c>b:
        print('C is Bigast')
    else:
        print('Both are semelar!')
a,b,c = map(int, input().split())
find_max(a, b, c)

# find bigast number in 3 numba (mathod 2)
def find(a,b,c):
    numbers = [a,b,c]
    # Sorting the list in ascending order
    numbers.sort(reverse=True)
    if a==numbers[0]:
        print('A is Bigast')
    elif b==numbers[0]:
        print('B is Bigast')
    elif c == numbers[0]:
        print('C is bigast')
a,b,c = map(int,input().split())
find(a,b,c)

# find bigast number in 3 numba (mathod 3)
def find_max(a,b,c):
    x = max(a,b,c)
    if x == a:
        print('A is Bigast')
    elif x == b :
        print('B is Bigast')
    elif x == c:
        print('C is Bigast')
a,b,c = map(int,input().split())
find_max(a,b,c)


