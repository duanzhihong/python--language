#堆分为最大堆和最小堆
#堆的排序属性：在堆中，对于具有父p的每个节点x，p中的键小于或者等于x的键，为最小堆
#大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
#小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
class BinHeap:
    #初始化堆
    def __init__(self):
        self.heapList = [0]  #初始化中添加一个0，方便以后的运算
        self.currentSize = 0 #当前堆的大小

    #重新定位元素，将新的元素放到合适的地方
    def percUp(self, i):    
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]: #如果当前的值小于它的父节点的值,进行替换
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp

        i = i//2

    #找到当前二叉树(三个节点)最小的节点元素的下标
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize: #从最后一个非子节点开始调整
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
        
    #保证节点还在合适的位置
    def percDown(self, i):
        while(i*2) <= self.currentSize: #遍历新的根节点下的所有二叉树
            mc =self.minChild(i)
            if  self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    #添加元素
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize+1
        self.percUp(self.currentSize) #将新的元素移动到合适的位置

    #删除根节点
    def delMin(self):
        retval = self.heapList[1] #要删除的根节点
        self.heapList[1] = self.heapList[self.currentSize] #将最后的节点放置到根结点上
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1) # 重新调整节点
        return retval 
    
    #利用列表构建堆 （堆排序）
    def buildHeap(self, arr):
        i = len(arr) // 2
        self.currentSize = len(arr)
        self.heapList = [0] + arr[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


bh = BinHeap()
bh.buildHeap([50, 16, 30, 10, 60,  90,  2, 80, 70])
print(bh.heapList)

