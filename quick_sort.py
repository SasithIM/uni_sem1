# def partition(list1):
#     index = 0
#     pivot = list1[-1]
#     less = []
#     great = []
#     for num in list1:
#         if num < pivot:
#             less.append(num)
#             index += 1
#         else:    
#             great.append(num)
#     list1=less + [pivot] + great
#     return index, list1


# def partition(list1):
#     index=0
#     pivot = list1[-1]
#     for i in range(len(list1)):
#         if list1[i] < pivot:
#             list1.insert(0, list1.pop(i))
#             index+=1
#     return list1.index(pivot)


# def quick_sort(list1):
#     if len(list1) < 2:
#         return list1
#     else:
#         pivot_index = partition(list1)
#         return quick_sort(list1[:pivot_index]) + [list1[pivot_index]] + quick_sort(list1[pivot_index+1:])


# def quick_sort(list1):# -> Any:
#     if len(list1) >= 2:
#         pivot_index = partition(list1)
#         return quick_sort(list1[:pivot_index]) + [list1[pivot_index]] + quick_sort(list1[pivot_index+1:])
#     else:
#         return list1


# def quick_sort(list1):
#     if len(list1) > 2:
#         pivot_index = partition(list1)
#         quick_sort(list1[:pivot_index])
#         quick_sort(list1[pivot_index+1:])

# import random

# random_list = [random.randint(1, 10) for _ in range(10)]
# print(random_list)

# quick_sort(random_list)

    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        less = []
        greater = []
        for i in arr:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)

l1=[7, 2, 3, 9, 10, 5, 7, 2, 7, 7]
print(l1)
l2 = quick_sort(l1)
print(l2)

# print(random_list)


