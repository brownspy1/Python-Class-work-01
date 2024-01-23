# Python Program to Display Fibonacci Sequence Using Recursion

def recarsiv(n):
    if n <= 1:
        return n
    else:
        return(recarsiv(n-1)+recarsiv(n-2))
num = int(input("Enter a number: "))
if num <=0:
    print("Sorry")
else:
    for i in range(num):
        print(recarsiv(i))