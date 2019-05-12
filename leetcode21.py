#@Time  : 2019/5/12 16:56
#@Author: Root
#@File  : leetcode21.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
        :param l1 : ListNode
        :param l2 : ListNode
        :return : ListNode
        """
        p1 = l1
        p2 = l2
        head = ListNode(0)
        end = head
        if not p1 and not p2 :
            return None
        while p1 and p2 :
            if p1.val == p2.val :
                end.next = p1
                end = end.next
                p1 = p1.next
                end.next = p2
                end = end.next
                p2 = p2.next
            elif p1.val < p2.val :
                end.next = p1
                end = end.next
                p1 = p1.next
            else :
                end.next = p2
                end = end.next
                p2 = p2.next
        if p1 :
            end.next = p1
        if p2 :
            end.next = p2
        head = head.next
        return head

    def better(self, l1, l2) :
        """
        采用递归求解更好
        :param l1:
        :param l2:
        :return:
        """
        if not l1 :
            return l2
        if not l2 :
            return l1
        t = None
        if l1.val <= l2.val :
            t = l1
            t.next = self.better(l1.next, l2)
        else :
            t = l2
            t.next = self.better(l1, l2.next)
        return t

l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(1)
l2.next = ListNode(3)
Solution().mergeTwoLists(l1, l2)