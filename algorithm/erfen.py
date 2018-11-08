#二分法，基于有序排列进行查找
import math
#while循环实现
def binarySearch(arr, item):
    low = 0
    height = len(arr)-1
    if arr[0] == item:
        return 0
    if arr[height] == item:
        return height
    while low<height:
        mid = (low+height)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            height = mid
        elif arr[mid] < item:
            low = mid
    return -1
#递归实现
def diguiSearch(arr, item, first, last):
    mid = (first+last)//2
    if (arr[mid] == item):
        return mid
    elif (arr[mid] > item):
        return diguiSearch(arr, item, first, mid-1)
    elif (arr[mid] < item):
        return diguiSearch(arr, item, mid+1, last)

arr = [1, 2, 4, 5, 6, 7, 8 ,9]
# location = diguiSearch(arr, 1, 0, 8)
location = binarySearch(arr,9)
print(location) 