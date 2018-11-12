#树的表示方法：
#可以使用列表进行表示
# myTree = ['a',
#             ['b', ['d', [], []],['e', [], []]],
#             ['c', ['f', [], []]]
#         ]
# print(myTree)
# print("left = ", myTree[1])
# print("root = ", myTree[0])
# print("right = ", myTree[2])

#每个节点都是一个对象
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    #插入左节点
    def inserLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode) #创建一个新的节点
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    #插入右节点
    def inserRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    #获取右孩子
    def getRightChild(self):
        return self.rightChild
    #获取左孩子
    def getLeftChild(self):
        return self.leftChild
    #获取根节点
    def setRootVal(self, obj):
        self.key = obj
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
# print(r.getLeftChild())

#添加左元素
r.inserLeft('b')
r.getLeftChild().inserLeft('d')
r.getLeftChild().inserRight('e')
# print(r.getLeftChild().getRootVal())

r.inserRight('c')
r.getRightChild().inserLeft('f')
r.getRightChild().inserRight('g')
#以上生成一个二叉树

def preorder(tree): #先序
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree): #中序
    if tree:
        postorder(tree.getLeftChild())
        print(tree.getRootVal())
        postorder(tree.getRightChild())
        
def nextorder(tree):
    if tree:
        nextorder(tree.getRightChild())
        nextorder(tree.getLeftChild())
        print(tree.getRootVal())

# preorder(r) 先序遍历
# postorder(r)
# nextorder(r)
# location = r.getRootVal()
# print(location)