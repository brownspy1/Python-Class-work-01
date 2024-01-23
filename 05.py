#chack number odd or evan
def chacker(number):
    if number%2 ==0:
        print(f'The number is even your number is {number}')

    else:
        print(f'The number is odd your number is {number}')

num = float(input())
chacker(num)