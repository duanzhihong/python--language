#堆排序 使用堆列实现
#堆排序：先创建大根堆，再进行交换和排序

#构建大根堆
def createBigHeap(arr, start, end):
    root = start #调整当前的二叉树的root下标设置为start
    while True:
        child = root*2 #当前二叉树的左孩子
        if child > end:
            break #没有子节点的时候结束构建 
        if child+1 <= end and arr[child] < arr[child+1]: #右孩子有效，同时找出左右孩子中比较大的数值的下标
            child += 1
        if arr[root] < arr[child]: #比较当前二叉树的根节点和孩子节点的大小，进行交换    
            arr[root], arr[child] = arr[child], arr[root]
            root = child 
        else:
            break

def heapSort(arr):
    first = len(arr)//2 - 1 #从最后一个非子节点开始构造大根堆
    for start in range(first, -1, -1):
        createBigHeap(arr, start, len(arr)-1)
    #首尾互换，依次得出最大的数字
    for end in range(len(arr)-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        createBigHeap(arr, 0, end-1)

arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
heapSort(arr)
print(arr)