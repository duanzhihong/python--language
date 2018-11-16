#选择排序改进了冒泡排序，它减少了冒泡的交换次数
def selectionSort(arr):
    for fillsort in range(len(arr)-1, 0, -1):
        positionMax = fillsort #假设最小的下标为0
        for location in range(1, fillsort+1):
            if arr[location] > arr[positionMax]:
                positionMax = location

        #进行位置交换,这里选择fillsort 是为了将大的数字放到后面
        tmp = arr[fillsort]        
        arr[fillsort] = arr[positionMax]
        arr[positionMax] = tmp

    return arr

arr = [1, 67, 52, 34, 87, 44]
arr2 = selectionSort(arr)
print(arr2)