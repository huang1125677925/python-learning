def quicksort(arr):
    if len(arr)>=2:
        temp=arr[0]
        left=[i for i in arr[1:] if i<=temp]
        right=[i for i in arr[1:] if i>temp]
    elif len(arr)==1:
        return arr
    else:
        return []
    
    return quicksort(left)+[temp]+quicksort(right)


quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

print(quicksort([5,7,8,10,90,100,200,3,-1]))