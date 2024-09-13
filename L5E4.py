from unittest.mock import ANY

columns=ANY
matrix = []
valid = True

while True:
    temp_input = input()
    if temp_input == '-1':
        break
    else:
        try:
            temp_list = list(map(int,temp_input.split()))
            if len(temp_list) == columns:
                matrix.append(temp_list)
                columns = len(temp_list)
            else:
                print('Invalid Matrix')
                valid=False
                break
        except:
            print('Invalid Matrix')
            valid=False
            break
print(matrix)

if valid:
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(columns)]
    print('\n'.join([' '.join(map(str,t_row)) for t_row in transpose]))