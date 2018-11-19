#冒泡，选择，插入，快排，二分，
def maopao(arr):
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr



#选择
def xuanze(arr):
    for i in range(len(arr)):
        minData = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minData]:
                i = j

        if arr[i] < arr[minData]:
            tmp = arr[i]
            arr[i] = arr[minData]
            arr[minData] = tmp  
    return arr


#插入
def charu(arr):
    for i in range(1,len(arr)):
        nowData = arr[i]
        position = i
        while arr[position-1] > nowData:
            arr[position] = arr[position-1] 
            position = position-1
        arr[position] =  nowData
    return arr

#快排
def kuaipai(arr):
    if len(arr) <= 1:
        return arr
    minData = arr[0]
    arr1 = []
    arr2 = []
    for i in range(1, len(arr)):
        if arr[i] <= minData:
            arr1.append(arr[i])
        if arr[i] > minData:
            arr2.append(arr[i])
    
    arr1 = kuaipai(arr1)
    arr2 = kuaipai(arr2)
    return arr1+[minData]+arr2

#广度优先遍历，深度优先遍历
class Graph:
    #表示图，使用字典，记录节点的个数，对应的数组里面保存相连的节点
    def __init__(self):
        self.nodeList = {} #节点的列表
        self.vistied = {} #访问过的节点
    def addNode(self, nodeArr):
        for i in nodeArr:
            if i not in self.nodeList.keys():
                self.nodeList[i] = []
    def createSide(self, edge):
        v,u = edge
        if u not in self.nodeList[v] and (v not in self.nodeList[u]):
            self.nodeList[v].append(u)
            self.nodeList[u].append(v)
    #广度遍历
    def breadthFirstSearch(self, node):
        queue = [] #模拟队列,广度遍历需要使用队列的数据结构
        sort = []
        if node:
            queue.append(node)
            queue.sort(node)
            self.bfs(node, queue, sort)
        return sort   
    def bfs(self, node, queue, sort):
        while len(queue) > 0:
            node = queue.pop(0)#出队列
            self.vistied[node] = True#记录已经访问过
            for i in self.nodeList[node]:
                if i not in queue and i not in sort:
                    queue.append(i)
                    sort.append(i)
    
    #深度遍历 递归遍历，访问一个节点后，继续访问该后面的节点
    def depthFirstSearch(self, node):
        sort = []
        if node:
            self.dfs(node, sort)
        return sort
    def dfs(self, node,sort):
        sort.append(node)
        self.vistied[node] = True
        for i in self.nodeList[node]:
            if i not in self.vistied:
                self.dfs(i, sort)

graph = Graph()
graph.addNode([1, 2, 3, 4, 5, 6, 7, 8])
graph.createSide((1, 2))
graph.createSide((1, 3))
graph.createSide((2, 4))
graph.createSide((2, 5))
graph.createSide((4, 8))
graph.createSide((5, 8))
graph.createSide((3, 6))
graph.createSide((3, 7))
graph.createSide((6, 7))
# sort1 = graph.breadthFirstSearch(1)
sort1 = graph.depthFirstSearch(1)
# print(sort1)
def createBigHeap(arr, start, end):
    nowRoot = start
    while True:
        child = nowRoot*2
        if child > end:
            break
        if (child+1 <= end) and (arr[child] < arr[child+1]):
            child = child+1
        if (arr[nowRoot] < arr[child]):
            arr[nowRoot], arr[child] = arr[child], arr[nowRoot]
            nowRoot = child
        else:
            break



#堆排序
def heapSort(arr):
    #创建大跟堆
    first = len(arr)//2
    for start in range(first, 0, -1):
        createBigHeap(arr, start, len(arr)-1)
    #堆排序
    for end in range(len(arr)-1, 0 , -1):
        arr[1], arr[end] = arr[end], arr[1]
        createBigHeap(arr, 1, end-1)
    return arr
arr = [0, 16, 7, 3, 20, 17, 8]
# result = heapSort(arr)
# print(result)

#希尔排序，归并排序
#希尔排序，通过使用增量
def xier(arr):
    grep = len(arr)//2
    while grep > 0:
        for i in range(grep):
            xierSort(arr, i, grep)
        grep = grep//2    

def xierSort(arr, i, grep):
    for j in range(i+grep, len(arr), grep):
        nowData = arr[j]
        nowPosition = j 
        while nowPosition > grep and arr[nowPosition-grep] > nowData:
            arr[nowPosition] = arr[nowPosition-grep]
            nowPosition = nowPosition-grep
        arr[nowPosition] = nowData

alist = [12,26,33,17,67,39,42,155,204]
xier(alist)
print(alist)

#归并排序
def guibing(arr):
    if len(arr) > 1:
        #分
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        guibing(leftArr)
        guibing(rightArr) 

        #治
        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i = i+1
            else:
                arr[k] = rightArr[j]
                j = j+1
            k = k+1
        #右侧数组已经全部放入了新数组中   
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i = i+1
            k = k+1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j = j+1
            k = k+1
    
arr = [54,26,93,17,77,31,44,55,20]
guibing(arr)
print(arr)