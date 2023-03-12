#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2 = head, head
        while pointer1 and pointer1.next:
            pointer2 = pointer2.next
            pointer1 = pointer1.next.next
            if pointer2 == pointer1:
                break
        else:
            return None
        pointer2 = head
        while pointer2 != pointer1:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer2    
# @lc code=end

