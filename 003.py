# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
           # l.append(head.val)
            l.insert(0,head.val)
            head = head.next
        return l

    def createlist(self, n):
        if n < 0:
            return False
        if n == 1:
            return ListNode(1)
        else:
            root = ListNode(1)
            tmp = root
            for i in range(2, n + 1):
                tmp.next = ListNode(i)
                tmp = tmp.next
        return root



if __name__ == '__main__':
    S = Solution()
    value = input()
    testNode = S.createlist(int(value))
    p = testNode
    while p!=None:
        print(p.val)
        p = p.next
    print(S.printListFromTailToHead(testNode))

