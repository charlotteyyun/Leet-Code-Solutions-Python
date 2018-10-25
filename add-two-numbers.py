"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = 0
        # adds the leading value of the linked lists l1 and l2 to integer ans
        if l1:
            ans += l1.val
        if l2:
            ans += l2.val
        # the succeeding values of the linked lists l1 and l2 are multiplied by 'mult', which increases by the factor of
        # 10 at every succeeding nodes
        mult = 10
        while l1.next:
            ans += l1.next.val * mult
            l1 = l1.next
            mult = mult*10
        mult =10
        while l2.next:
            ans += l2.next.val*mult
            l2 = l2.next
            mult = mult*10

        # integer ans is converted to a string and is reversed.
        ans = str(ans)[::-1]
        # a linked list is formed such that digits in ans are linked in order
        n = ListNode(ans[0])
        i = 1
        ne = n
        while i < len(ans):
            ne.next = ListNode(ans[i])
            ne = ne.next
            i +=1
        return n
