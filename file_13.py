# This Program by m.mahadi program number 13
# 100+90+80+70+60+...+n
def seres(n):
    add = 0
    for i in range(n, 0, -10):
        add += i
        print(add)


n = int(input())
seres(n)
