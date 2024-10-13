def selection_sort_three_passes(arr):
    n = len(arr)
    arr = arr.copy()
    
    for i in range(3):  # Only do first 3 iterations
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Selection Sort after pass {i+1}: {arr}")
    
    return arr

def bubble_sort_three_passes(arr):
    n = len(arr)
    arr = arr.copy()
    
    for i in range(3):  # Only do first 3 iterations
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Bubble Sort after pass {i+1}: {arr}")
    
    return arr

# Test array
test_arr = [64, 34, 25, 12, 22, 11, 21]
print(f"Original array: {test_arr}")
print("\nSelection Sort:")
selection_result = selection_sort_three_passes(test_arr)
print("\nBubble Sort:")
bubble_result = bubble_sort_three_passes(test_arr)