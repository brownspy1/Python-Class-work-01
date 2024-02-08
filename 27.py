# This Program by m.mahadi 
# Largast and semilast elimat in arrye
set = [10, 324, 45, 90, 9808]
print(max(set))


# Largast and semilast elimat in arrye 02

def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


# for run program input exmp 10 20 50 40 20 30 80 45
set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(set)
num = largest(set, n)
print(num)
