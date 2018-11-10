#希尔排序
#通过使用增量，是插入排序的升级(while循环和递归)
def shellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(arr, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(arr, start, gap):
    #插入排序
    for i in range(start+gap, len(arr), gap): #比较分组好的数字
        currentvalue = arr[i]
        position = i
        while position>=gap and arr[position-gap]>currentvalue:
            arr[position] = arr[position-gap]
            position = position-gap
        
        arr[position] = currentvalue

#希尔排序的时间复杂度介于常数和平方之间
alist = [12,26,33,17,67,39,42,155,204]
shellSort(alist)
print(alist)