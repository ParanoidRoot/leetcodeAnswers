#@Time  : 2019/5/13 21:51
#@Author: Root
#@File  : leetcode24.py


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head : ListNode) :
        """
        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        :param head : ListNode
        :return : ListNode
        """
        if not head :
            return None
        p0 = None
        p1 = head
        p2 = head.next
        if not p2:
            return head
        ansHead = p2
        p1.next = p0
        p0 = p1
        p1 = p2
        p2 = p2.next
        p1.next = p0
        p0.next = p2
        p1 = p2
        if p1 :
            p2 = p2.next
        else :
            return ansHead
        lastNode = p0
        while p1 :
            p1.next = p0
            p0 = p1
            p1 = p2
            if p1 :
                # 代表有下一个
                p2 = p2.next
                p1.next = p0
                p0.next = p2
                lastNode.next = p1
                p1 = p2
                if p1 :
                    p2 = p2.next
                    lastNode = p0
                else :
                    break
            else :
                # 代表没有下一个
                p0.next = p1
        return ansHead

    def better(self, head : ListNode) :
        """
        递归法求解，思路更加清晰
        :param head:
        :return:
        """
        if not head or not head.next :
            return head
        t = head.next
        head.next = self.better(t.next)
        t.next = head
        return t


