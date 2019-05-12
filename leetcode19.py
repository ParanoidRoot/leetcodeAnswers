#@Time  : 2019/5/12 16:28
#@Author: Root
#@File  : leetcode19.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n) :
        """
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        p = head
        index = 0
        while index < n :
            p = p.next
            index += 1
        pre = None
        cur = head
        while p :
            p = p.next
            pre = cur
            cur = cur.next
        if not pre :
            head = head.next
            cur.next = None
            del cur
        else :
            pre.next = cur.next
            cur.next = None
            del cur
        return head


