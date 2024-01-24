# This Program by m.mahadi program number 12
# 5+10+15+20....+n
def seres(n):
    add = 0
    for i in range(1,n+1):
        if i %5 == 0:
            add +=i
            print(add)
n = int(input())
seres(n)