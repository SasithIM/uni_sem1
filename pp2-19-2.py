import string 

alp = string.ascii_lowercase+' '

n = 3
key = [[3,8,12],[23,4,1],[21,19,5]]

def matrix_mul(mat_a,mat_b):
    temp_mat = []
    for i in range(len(mat_a)):
        temp = 0
        temp_mat.append([])
        for j in range(len(mat_b[0])):
            for k in range(len(mat_a[0])):
                temp += mat_a[i][k]*mat_b[k][j]
            temp_mat[i].append(temp%27)
    return temp_mat

def create_msg(string:str):
    msg = []
    if len(string)<n:
        string+=' '*(n-len(string))
    for i in string.lower():
        if i in alp:
            msg.append([alp.index(i)])
    return msg

print(*[alp[i[0]] for i in matrix_mul(key,create_msg('AB'))],sep='')