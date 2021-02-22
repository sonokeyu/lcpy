#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 快速排序
        if not head: return None
        # small equal large 的缩写
        # 都指向相应链表的 head
        s = e = l = None
        target = head.val
        while head:
            nxt = head.next
            if head.val>target:
                head.next = l
                l = head
            elif head.val==target:
                head.next = e
                e = head
            else:
                head.next = s
                s = head
            head = nxt
        
        s = self.sortList(s)
        l = self.sortList(l)
        # 合并 3 个链表
        dummy = ListNode(0)
        cur = dummy # cur: 非 None 的尾节点
        # p: 下一个需要连接的节点
        for p in [s, e, l]:
            while p:
                cur.next = p
                p = p.next
                cur = cur.next
        return dummy.next
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    vals = [9, 2, 3, 4, 8, 1, 7]
    head = ListNode()
    next_node = head
    # print(type(head.val))
    # print(type(next_node.val), "*****")
    next_node = head
    for i in vals:
        # print(i)
        next_node.val = i
        j = ListNode()
        next_node.next = j
        next_node = j
    # print(head)
    # index = head
    # while(index.next):
    #     print(index.val, "+++++")
    #     index = index.next
    a = s.sortList(head)
    print(a)
    
