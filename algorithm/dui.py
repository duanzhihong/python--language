#堆排序 使用堆列实现
#堆排序：先创建大根堆，再进行交换和排序
def createBigHeap(arr, start, end):
    nowRoot = start
    while True:
        child = nowRoot*2 #当前二叉树的孩子节点
        if child > end:
            break
        if (child+1 <= end) and (arr[child] < arr[child+1]): #如果存在右孩子，从左右孩子中选取值大的节点
            child = child+1
        if (arr[nowRoot] < arr[child]):
            arr[nowRoot], arr[child] = arr[child], arr[nowRoot]
            nowRoot = child 
        else:
            break



#堆排序
def heapSort(arr):
    #创建大根堆
    first = len(arr)//2
    for start in range(first, 0, -1):#第一个数字为0，占位符号
        createBigHeap(arr, start, len(arr)-1)
    #堆排序， 首尾交换，继续构建大根堆
    for end in range(len(arr)-1, 0 , -1):
        arr[1], arr[end] = arr[end], arr[1]
        createBigHeap(arr, 1, end-1)
    return arr
arr = [0, 16, 7, 3, 20, 17, 8]
result = heapSort(arr)
print(result)