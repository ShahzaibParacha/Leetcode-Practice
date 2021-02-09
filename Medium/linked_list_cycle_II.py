# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head):
        
        slow = head
        fast = head.next
        loop = None
        
        while slow is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop = fast
        if loop is None:
            return None
        
        slow = head
        while slow != loop:
            slow = slow.next
            if loop.next is None:
                return None
            else:
                loop = loop.next

        return slow.val
    
headnode = ListNode(-4)
headnode.next = (ListNode(0))
headnode.next.next = (ListNode(2))
headnode.next.next.next = (ListNode(3))

s = Solution()
print(s.detectCycle(headnode))

# Works!