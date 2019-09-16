# 查找某个数值位置
def binsearch(arr,x):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x: return mid
        elif arr[mid]>x: right=mid-1
        else: left=mid+1
    
    return -1

# 查找大雨等于x的第一个数值
def binsearch1(arr,x):
    left, right = 0, len(arr) - 1
    # 这个地方不能等于，等于可能会形成死循环
    while left<right:
        # 默认往下取整
        mid = (left + right) // 2
        if arr[mid] >= x:
            # 因为有可能当前中间点之前还有大于等于x的数存在
            right = mid
        else:
            left = mid + 1
    
    return left


# 查找小于等于x的第一个值
def binsearch3(arr, x):
    import math
    left, right = 0, len(arr) - 1
    # 这个地方不能等于，等于可能会形成死循环
    while left <right:
        mid = math.ceil((left + right) / 2)
        # if arr[mid]==x: return mid
        if arr[mid] > x:
            # 因为有可能当前中间点之前还有大于等于x的数存在
            right = mid-1
        else:
            left = mid
    
    return right






# 查找大雨x的第一个数值
def binsearch2(arr, x):
    left, right = 0, len(arr) - 1
    # 这个地方不能等于，等于可能会形成死循环
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            # 因为有可能当前中间点之前还有大于等于x的数存在
            # 不用mid也不行，因为前面有可能数小于x
            right = mid
        else:
            left = mid + 1
    
    return left


print(binsearch3([1,4,5,6,7,8,8,8,10],9))