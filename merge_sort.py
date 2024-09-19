import random

def merge(list1,list2):
    index = 0
    while index<len(list1) and list2:
        if list2[0] < list1[index]:
            list1.insert(index,list2.pop(0))
        else:
            index += 1
    list1.extend(list2)
    return list1   


# #test cases for merge
# print(merge([1,2,3,4],[2,3,4,5]))
# print(merge([1,2,3,4],[5,6,7,8]))
# print(merge([1,2,3,4],[0,1,2,3]))
# print(merge([1,2,3,4],[4,5,6,7]))


def merge_sort(list1):
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1)//2
        return merge(merge_sort(list1[:mid]),merge_sort(list1[mid:]))
    

#test cases for merge_sort
# Generate a random list of integers
random_list = [random.randint(0, 100) for _ in range(10)]

# Print the unsorted random list
print(random_list)

# Sort the random list using merge_sort
sorted_list = merge_sort(random_list)

# Print the sorted list
print(sorted_list)