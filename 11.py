# This Program by m.mahadi program number 11
# 2+4+6+8+....+n
def seres(n):
    add = 0
    for i in range(1,n+1):
        if i %2 == 0:
            add +=i
            print(add)
n = int(input())
seres(n)