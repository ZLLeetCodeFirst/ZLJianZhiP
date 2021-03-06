# -*- coding:utf-8 -*-
l = []
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1+pos],tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])
        return root
    def front_digui(self, root):
        if root == None:
            return None
        else:
            l.append(root.val)
            self.front_digui(root.left)
            self.front_digui(root.right)

if __name__ == '__main__':
    S = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    root = S.reConstructBinaryTree(pre,tin)
    S.front_digui(root)
    print(l)
