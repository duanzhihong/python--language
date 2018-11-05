#哈希算法：
# 余数方法：数据除以表长，使用余数作为散列值
# 分组求和法：把数据分成大小相等的块，想加之后求出散列值 
# 平方取中法： 数据的平方取其中两位数
#实现map
class hTable():
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots)) #创建哈希值
        if self.slots[hashvalue] == None: #创建hash映射
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key: #旧数据替换新数据
                self.data[hashvalue] = data
            else: #解决hash冲突
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if  self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data 

    def hashfunction(self, key, size):
        return key%size
    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key): #查找hash函数
        startSlot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot #起始值
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data
    
    # 魔术方法 getitem setitem
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key,data)

H = hTable()
H[54] = 'cat'
H[26] = 'dog'
H[54] = 'pig'
print(H.slots)
print(H.data)