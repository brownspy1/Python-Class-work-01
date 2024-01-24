# This Program by m.mahadi program number 10
#1+2+3+4....+n
def seres(n):
    add = 0
    for i in range(1,n+1):
        add +=i
        print(add)
n = int(input())
seres(n)