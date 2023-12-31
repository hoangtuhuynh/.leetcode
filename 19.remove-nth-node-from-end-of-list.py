#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        left = temp
        right  = head
        while n >0:
            right = right.next
            n-=1
        while right:
            right - right.next
            left = left.next

        # delete
        left.next = left.next.next
        return temp.next

# @lc code=end

