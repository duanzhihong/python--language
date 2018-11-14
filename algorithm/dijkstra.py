#构建有向图
G = {
    1:{1:0, 2:1, 3:12},
    2:{2:0, 3:9, 4:3},
    3:{3:0, 5:5},
    4:{4:0, 3:4, 5:13, 6:15},
    5:{5:0, 6:4},
    6:{6:0}
}


#每次找到一个当前点最近的点，然后对该点进行扩展
#计算出起始点到所有点的最短距离
#一种贪婪算法
#无法解决带负权值的图

def dijkstra(G, v0, INF = 999):
    book = set() #记录走过的距离点
    minv = v0

    #源点到其余各个顶点的起始路程 (默认为无穷大，后续依次进行计算)
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0 #到达自身的距离为0
    while len(book) < len(G):
        book.add(minv) #确定当前定点的距离
        for w in G[minv]: #当前点的邻居点
            if dis[minv] + G[minv][w] < dis[w]: #如果扩展到邻居点的距离 小于 已知距离
                dis[w] = dis[minv] + G[minv][w] #更新已知距离

        #选择剩余中最小的距离点作为新的扩散点
        new = INF 
        for v in dis.keys():
            if  v in book: continue
            if dis[v] < new:
                new = dis[v]
                minv = v                
    return dis


dis = dijkstra(G, 1)
print(dis)