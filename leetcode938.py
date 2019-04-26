#@Time  : 2019/4/26 16:40
#@Author: Root
#@File  : leetcode938.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) :
        """
        返回二叉搜索樹之間的所有值
        :param root:
        :param L:
        :param R:
        :return:
        """
        if root == None :
            return 0
        if root.val > L and root.val < R :
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)
        elif root.val == L :
            return root.val + self.rangeSumBST(root.right, L, R)
        elif root.val == R :
            return self.rangeSumBST(root.left, L, R) + root.val
        elif root.val < L :
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R :
            return self.rangeSumBST(root.left, L, R)