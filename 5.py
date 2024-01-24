# # This Program by m.mahadi program number 5
# # prime numbar print
prime = []


def is_prime(n):
    for number in range(2, n + 1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime.append(number)


is_prime(100)
print(prime)

# chack It's prime or not
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

n = int(input())
if is_prime(n):
    print("It is a prime number")
else:
    print("is not a prime number")
