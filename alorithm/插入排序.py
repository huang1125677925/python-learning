def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        print(preIndex,current)
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr


# 还是这个方法简单的多，
def insetionNum(arr):
    if len(arr)==1:
        return arr
    
    for i in range(1,len(arr)):
        temp,j=arr[i],i
        while j>0 and temp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=temp
        
    
    return arr


print(insetionNum([5,4,3,2,7,8]))