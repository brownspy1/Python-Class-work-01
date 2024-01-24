# This Program by m.mahadi 
#add and substrac matrix
matrix_3 = [[0,0,0],[0,0,0],[0,0,0]]
def add_matrix(matrix_1,matrix_2):
    for i in range(len(matrix_1)):
        for x in range(len(matrix_1[0])):
            matrix_3[i][x] = matrix_1[i][x] + matrix_2[i][x]
    print(matrix_3)
def subtract_matrix(matrix_1,matrix_2):
    for i in range(len(matrix_1)):
        for x in range(len(matrix_1[0])):
            matrix_3[i][x] = matrix_1[i][x] - matrix_2[i][x]
    print(matrix_3)
matrix_1 =[
    [2,5,8],
    [3,6,9],
    [7,4,1]
]
matrix_2 = [
    [3,2,1],
    [8,5,6],
    [8,6,2]
]
# add 1 and 2 matrix
add_matrix(matrix_1,matrix_2)
# substrac 1 and 2 matrix
subtract_matrix(matrix_1,matrix_2)