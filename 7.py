# This Program by m.mahadi program number 7
# febonacce seres

febo = [0,1]

def fibo(n):
    if n <= 0 or n <= 1:
        return n
    else:
        for i in range(2,n + 1):
            febo.append(febo[i - 1] + febo[i - 2])
    print(f'Your febo seres is : {febo}')

n = int(input())
fibo(n)
