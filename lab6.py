from typing import Any

# # uncomment before use
# n, m =map(int,input('Enter the dimensions: ').split(','))

def mat_in(n:int,m:int,name:str):
    print(f'Enter Matrix {name}:')
    mat=[]
    for i in range(n) :
        try:
            row=list(map(int,input().split(' ')))
        except :
            print('Error')
            return -1
        if len(row)==m:
            mat+=[row]
        else:
            print(row)
            print('Invalid Matrix')
            return -1
    else:
        return mat
            
matrix_A = [[1, 2, 3, 4], [3, 3, 4, 4], [4, 4, 5, 5]]
matrix_B = [[1, 7, 3, 3], [3, 7, 4, 4], [5, 7, 5, 5]]
# print(matrix_A)


def mat_trans(matrix:list[list]) -> list[list]:
    return [list(i) for i in zip(*matrix)]

# print(mat_trans(matrix_A))

def mat_mul(n,m,mat_a:list[list], mat_b:list[list])->list[list]:
    mat_b = mat_trans(mat_b)
    mat_c=[list() for i in range(n)]
    c=0
    for k in range(n*n*m):
        c += mat_a[k//(n*m)][k%m]*mat_b[k%m][(k//m)%n]
        if not (k+1)%m:
            mat_c[k//(n*m)].append(c)
            print(k//(n*m),c)
            c=0
    else:
        return mat_c
    
print(mat_mul(3,4,matrix_A,matrix_B))