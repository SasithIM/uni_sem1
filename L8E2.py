def mat_minor(matrix, i, j):
    print(i,j, matrix)
    temp_matrix = matrix[:i]+matrix[i+1:]
    for index in range(len(matrix)-1):
        temp_matrix[index] = temp_matrix[index][:j]+temp_matrix[index][j+1:]
    return temp_matrix

# determinants
def mat_det(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        return sum([((-1)**(i))*matrix[0][i]*mat_det(mat_minor(matrix, 0, i)) for i in range(len(matrix))])
    

matrix1 = [[1, 0, 1], [8, 7, 5], [6, 5, 3]]
print(matrix1)
print(mat_det(matrix1))