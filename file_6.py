# This Program by m.mahadi program number 6
# print factorial value of a number
def factoial(n):
    fact = 1
    for x in range(1,n+1):
        fact *=x
        print(fact)
n = int(input("Enter:"))
factoial(n)
