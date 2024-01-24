# This Program by m.mahadi program number 16

def seres(n):
    add = 1
    for i in range(1,n+1):
        if i %2 == 0:
            add +=1/i
            print(add)
n = int(input())
seres(n)