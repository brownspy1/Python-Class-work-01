# This Program by m.mahadi 
# make programm using recarsiv funtion
def reacrsiv_fun(n):
    if n == 1:
        return n
    else:
        return n * reacrsiv_fun(n - 1)


number = int(input("Enter a number: "))

# chacking zone
if number < 0:
    print("Negative")
elif number == 0:
    print(0)
else:
    print(reacrsiv_fun(number))
