#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def full_adder(self, Ci, add, added):
        return int((Ci + add + added)%10), int((Ci + add + added)/10)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        sum = ListNode(0)
        temp = sum
        Co = 0
        while 1:
            add = a.val if a.val + 1 else 0
            added = b.val if b.val + 1 else 0
            val, Co = self.full_adder(Co, add, added)
            temp.val = val
            a = a.next if a.val>-1 and a.next else ListNode(-1)
            b = b.next if b.val>-1 and b.next else ListNode(-1)
            if not (a.val + 1 or b.val + 1):
                if Co:
                    temp.next = ListNode(Co)
                    break
                break
            temp.next = ListNode(0)
            temp = temp.next
        return sum
            
        
# @lc code=end

