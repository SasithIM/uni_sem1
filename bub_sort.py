def bub_sort(in_list):
    not_sorted = True
    # min_index = 0
    while not_sorted:
        not_sorted = False
        for i in range(len(in_list)-1):
            if in_list[i] > in_list[i+1]:
                in_list[i],in_list[i+1] = in_list[i+1],in_list[i]
                not_sorted = True
    return in_list


# import random
# rand_list = [random.randint(1, 100) for _ in range(10)]
# print(rand_list)


# print(bub_sort(rand_list))