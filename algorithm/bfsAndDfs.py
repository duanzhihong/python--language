#bfs 广度遍历
#dfs 深度遍历

#创建图
class Graph:
    def __init__(self):
        self.nodeNeighbors = {} #节点的邻居
        self.vistied = {} #访问的节点记录

    #添加节点
    def addNodes(self, nodeList):
        for node in nodeList:
            if node not in self.nodeNeighbors.keys():
                self.nodeNeighbors[node] = []
    
    #添加边，创建无向图(邻接表)
    def createGraph(self, edge):
        v,u = edge
        if (v not in self.nodeNeighbors[u]) and (u not in self.nodeNeighbors[v]):
            self.nodeNeighbors[v].append(u)
            self.nodeNeighbors[u].append(v)

    #广度优先遍历 使用队列的结构
    def breadthFirstSearch(self, node):
        sort = []
        queue = []
        if node:
            queue.append(node)
            sort.append(node)
            self.bfs(node, queue, sort)
        return sort

    def bfs(self, node, queue, sort):
        while len(queue) > 0:
            node = queue.pop(0) #从列表中取出访问的元素
            self.vistied[node] = True

            for n in self.nodeNeighbors[node]:
                if (not n in self.vistied) and (not n in queue):
                    queue.append(n)
                    sort.append(n)
        
    #深度优先遍历 递归使用栈的结构
    def depthFirstSearch(self, node):
        sort = []
        if node:
            self.dfs(node, sort)
        return sort

    def dfs(self, node, sort):
        self.vistied[node] = True
        sort.append(node)
        for n in self.nodeNeighbors[node]:
            if not n in self.vistied:
                self.dfs(n,sort)
    


graph = Graph()
nodeList = [i+1 for i in range(8)]
graph.addNodes(nodeList)
graph.createGraph
graph.createGraph((1, 2))
graph.createGraph((1, 3))
graph.createGraph((2, 4))
graph.createGraph((2, 5))
graph.createGraph((4, 8))
graph.createGraph((5, 8))
graph.createGraph((3, 6))
graph.createGraph((3, 7))
graph.createGraph((6, 7))
print(graph.nodeNeighbors)
# sort1 = graph.breadthFirstSearch(1)
sort1 = graph.depthFirstSearch(1)
print(sort1)
