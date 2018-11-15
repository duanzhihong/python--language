# 您将获得两个非空链表，表示两个非负整数。数字以相反的顺序存储，每个节点包含一个数字。添加两个数字并将其作为链接列表返回。
# 您可以假设这两个数字不包含任何前导零，除了数字0本身
# 输入：（2  - > 4  - > 3）+（5  - > 6  - > 4）
#  输出： 7  - > 0  - > 8
#  说明： 342 + 465 = 807。

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = listNode(0) #初始化链表，创建节点
        while l1 or l2 or carry:
            v1 = v2 = 0 #初始化链表的初始值
            if l1;
                v1 = l1.val #获取链表的值
                l1 = l1.next #链表的指向为下一个
            if l2:
                v2 = l2.val 
                l2 = l2.next 
            carry, val = divmod(v1+v2+carry, 10) #获取商和余数
            n.next = listNode(val) #添加节点
            n = n.next
    return root.next
