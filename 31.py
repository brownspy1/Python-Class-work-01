# This Program by m.mahadi
def add_num(a, b):
    add = a + b
    sd = str(a)
    st = str(b)
    print(f'Addition is {add}\nadd is {str(sd+st)}')


a, b = map(int, input().split())
add_num(a, b)
