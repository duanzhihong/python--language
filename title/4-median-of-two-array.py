#两个数组的中位数
# 有两个排序的数组nums1和nums2分别为m和n。
# 找到两个排序数组的中位数。总运行时间复杂度应为O（log（m + n））。
# 您可以假设nums1和nums2  不能都为空。
# 例1：
# nums1 = [1,3]
# nums2 = [2]
# 中位数是2.0
# 例2：
# nums1 = [1,2]
# nums2 = [3,4]
# 中位数为（2 + 3）/ 2 = 2.5


class find:

    def __init__(self):
        pass

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B) #计算总长度，有可能两个序列的长度不同
        if l % 2 == 1: #总数为奇数
            return self.kth(A, B, l // 2)
        else: #总数为偶数
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1))/2
    #计算中位数
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) //2 #a和b序列的中位数的下标
        ma, mb = a[ia], b[ib] #a，b的中位数
        if ia + ib < k: #是否需要重新计算k的值
            if ma > mb: #重新计算，当ma>mb时候，b的数组取较大部分，同时修改k的值
                return self.kth(a, b[ib+1: ], k - (ib + 1))
            else: 
                return self.kth(a[ia+1:], b, k - (ia + 1))
        else:
            if ma > mb:
                a = a[:ia]
            else:
                b = b[:ib]
            return self.kth(a, b, k)

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10, 11]
c = find()

midth = c.findMedianSortedArrays(a, b)
print(midth)