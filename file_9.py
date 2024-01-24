# This Program by m.mahadi program number 9
# Grading system
def GPA(n):
    if 80 <= n <= 100:
        print(f'Congratulations! You Got A+\nYour GPA is {n}')
    elif 70 <= n <= 79:
        print(f'Congratulations! You Got A\nYour GPA is {n}')
    elif 60 <= n <= 69:
        print(f'Congratulations! You Got B\nYour GPA is {n}')
    elif 50 <= n <= 59:
        print(f'Congratulations! You Got C\nYour GPA is {n}')
    elif 40 <= n <= 49:
        print(f'Good! You Got D\nYour GPA is {n}')
    elif 33 <= n <= 39:
        print(f'Good! You Got E\nYour GPA is {n}')
    elif 0 <= n <= 32:
        print(f'oops! You Got F\nYour GPA is {n}')

n = float(input('Enter GPA:'))
GPA(n)
