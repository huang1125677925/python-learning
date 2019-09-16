def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=arr[:mid],arr[mid:]
    return merge(mergeSort(left),mergeSort(right))


def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result.extend(left)
    if right:
        result.extend(right)
        
    return result



print(mergeSort([0,1,-9,100,34,87,2,-100,93,200]))