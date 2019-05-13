#@Time  : 2019/5/13 20:48
#@Author: Root
#@File  : leetcode23.py

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x) :
        self.val = x
        self.next = None

class Solution:

    """
    dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next
    """
    def mergeKLists(self, lists) :
        """
        合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
        :param lists : List[ListNode]
        :return : ListNode
        """
        if not lists :
            return None
        ansHead = ansEnd = ListNode(0)
        q = []
        for index in range(len(lists)) :
            if lists[index] :
                heapq.heappush(q, (lists[index].val, index) )
                lists[index] = lists[index].next
        while q :
            value, index = heapq.heappop(q)
            ansEnd.next = ListNode(value)
            ansEnd = ansEnd.next
            if lists[index] :
                heapq.heappush(q, (lists[index].val, index))
                lists[index] = lists[index].next
        ansEnd.next = None
        return ansHead.next