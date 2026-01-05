def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # last element as pivot
    left = []
    right = []
    
    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
