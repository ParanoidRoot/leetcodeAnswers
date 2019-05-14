#@Time  : 2019/5/14 13:28
#@Author: Root
#@File  : leetcode25.py


# Definition for singly-linked list.
class ListNode :
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode :
        """
        给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
        k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
        :param head : 头节点
        :param k : k个一组
        :return : 反转后的头结点
        """
        if not head :
            return head
        p1 = head
        p2 = p1
        pre = None
        i = 0
        while i < k and p2 :
            pre = p2
            p2 = p2.next
            i += 1
        if i < k :
            return head
        p2 = pre.next = self.reverseKGroup(p2, k)
        previousNode = p2
        currentNode = p1
        nextNode = p1.next
        while True :
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            if currentNode == p2 :
                return previousNode
            else :
                nextNode = nextNode.next

t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(5)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
t5.next = None

Solution().reverseKGroup(t1, 2)