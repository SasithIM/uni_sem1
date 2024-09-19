
#slection sort algorithm
def sel_sort(in_list:list):
    for i in range(len(in_list)):
        t = min(in_list[i:])
        in_list[in_list.index(t)],in_list[i]=in_list[i],t
    return in_list


# import random as r

# #make a random list to test the algorithm
# rand_list = [r.randint(1, 100000) for _ in range(1000)]
# print(rand_list)

# print(sel_sort(rand_list))