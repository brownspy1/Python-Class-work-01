# This Program by m.mahadi 
from functools import lru_cache

@lru_cache(maxsize=1000)
# Python Program to Display Fibonacci Sequence Using Recursion
# souse https://youtu.be/Qk0zUZW-U_M?si=Qz3PFhaeAFYg0i1Q
def recarsiv(n):
    if n <= 1:
        return n
    else:
        return recarsiv(n - 1) + recarsiv(n - 2)


add = int(input("Enter a number: "))

if type(add) != int:
    print("Invalid number!")
elif add <= 0:
    print("0")
else:
    for x in range(add + 1):
        print(x, ':', recarsiv(x))