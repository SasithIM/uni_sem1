#get the input
number_list = [eval(i) for i in input().split()]

#set the min and max values to be the first value
max_num, min_num = number_list[0],number_list[0]

for number in number_list:
    if number - min_num < 0:
        min_num=number
    elif max_num - number < 0:
        max_num=number 
        
print(f'Minimum = {min_num}\nMaximum = {max_num}')