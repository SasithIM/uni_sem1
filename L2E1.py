# angles=[] #a list to store the angles

# #get three angles
# for i in range(3):
#     angles.append(float(input(f'Enter angle {i+1}')))

# #sort angles list from smallest to largest
# angles.sort()

# #check if angles form a triangle
# if sum(angles)==180:    

#     #check if right angled
#     if angles[-1] == 90:    
#         print('Right angled')

#     #check if Obtuse angled
#     elif angles[-1] > 90:   
#         print('Obtuse angled')

#     #if neither above, it is acute angled
#     else:
#         print('Acute angled')

# #if angles does not sum to 180, they can't form a triangle
# else:
#     print('Angles do not form a triangle')  

# get input
a_list = [float(input(f'Enter angle {i+1}: ')) for i in range(3)]

# sort the list in descending order
a_list.sort(reverse=True)

# check whether angles form a triangle
if a_list[-1]>0 and sum(a_list) == 180:

    # decide obtuse, right or acute from the largest angle of the three
    if a_list[0]>90:
        print('Obtuse angled')
    elif a_list[0]==90:
        print('Right angled')
    else:
        print('Acute angled')

else:
    print('Angles do not form a triangle')