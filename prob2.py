__author__ = 'windmgc'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        real1 = 0
        real2 = 0
        flag = 0
        while l1 is not None:
            real1 += l1.val * 10 ** flag
            flag += 1
            l1 = l1.next
        flag = 0
        while l2 is not None:
            real2 += l2.val * 10 ** flag
            flag += 1
            l2 = l2.next
        realsum = real1 + real2
        print realsum
        l3 = ListNode(0)
        l4 = l3
        while realsum >= 10:
            l3.val = realsum % 10
            realsum = (realsum - l3.val) / 10
            l3.next = ListNode(0)
            l3 = l3.next
        l3.val = realsum
        return l4