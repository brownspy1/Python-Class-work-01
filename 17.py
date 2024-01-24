# This Program by m.mahadi program number 17

def seres(n):
    add = 1
    for i in range(1,n+1):
        if i %2 == 0:
            add +=1/i**2
            print(add)
n = int(input())
seres(n)