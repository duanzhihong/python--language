#插入排序
#每次排序会直接找到合适的位置进行排序
def insertSort(arr):
    for index in range(1, len(arr)):
        currentvalue = arr[index] #从第二个数开始，与第一个数进行比较，第三个数，与前面两个比较，找到合适的地方，然后依次进行
        position = index #为了将数字排序，记录当前比较的索引

        while arr[position-1] > currentvalue and position>0:
            arr[position] = arr[position-1]#移动位置
            position = position-1
        #将当前比较的值放到合适的位置
        arr[position] = currentvalue
    return arr

arr = [23,12,32,45,39,67,43,86,4]
sortArr = insertSort(arr)
print(sortArr)