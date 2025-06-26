# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast= head

        while fast and fast.next:

            slow= slow.next
            fast= fast.next.next

            if slow== fast:
                return True
        
        return False


"""
If I am asked to find mid or check cycle, I need to use slow and fast pointers (2 pointers)

Slow moves one step at a time and fast moves 2 steps. 
if there is cycle, at once point slow and fast will point to same node. Then, I can conclude that cycle exists. 

while loop until fast and fast.next is null

"""