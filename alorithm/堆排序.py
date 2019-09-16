def buildMaxHeap(arr):
    import math
    # 初始化建堆，先从导数第二层点开始，
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr


print(heapSort([1,9,0,-1,-4,43,100]))

def build(arr):
    for i in range(len(arr)//2,-1,-1):
        next_down(arr,i)
        
def next_down(arr,i):
    left=2*i
    right=2*i+1
    
    largest=i
    if left<arrlen and arr[left]>arr[i]:
        largest=left
    if right<arrlen and arr[right]>arr[i]:
        largest=right
    if largest!=i:
        swap(arr,largest,i)
        next_down(arr,largest)

def heapSort(arr):
    global arrlen
    arrlen=len(arr)
    build(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,i,0)
        arrLen-=1
        next_down(arr,0)
