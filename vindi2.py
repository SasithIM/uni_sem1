INPUT_FILE_NAME = 'testmatrix.txt'
########################################################################################
# Do not change anything above this line
########################################################################################

# Use INPUT_FILE_NAME variable to read the file instead of 'matrix_data.txt'
# Enter your code here

def get_matrix(data_list,index=1):
    matrices = []
    
    if index >= len(data_list):
        return matrices
        
    else:
        no_of_rows = int(data_list[index])
        matrix = []
        for i in range(index+1,no_of_rows+index+1):
         
            matrix.append(list(map(int,data_list[i].split(','))))
    
        matrices.append(matrix)
    
        print(matrices)
        index += no_of_rows + 1
    
    remaining  = get_matrix(data_list,index)
    
    return matrices + remaining
    
    
with open(INPUT_FILE_NAME) as data:
    demo = data.read()
    data_list = demo.split()
    print(data_list)
    
data_matrix = get_matrix(data_list)
print(data_matrix)