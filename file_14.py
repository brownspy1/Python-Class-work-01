# This Program by m.mahadi program number 14

def seres(n):
    add = 0
    for i in range(1,n+1):
        if i %2 == 0:
            add +=i**2
            print(add)
n = int(input())
seres(n)