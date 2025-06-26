# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        # 1. create dummy node
        dummy = ListNode(0, head)

        #assign left to dummy and right to head
        left= dummy 
        right = head

        # 2. go to correct right position. offset n between left and right 
        while n>0 and right: #(right is not null)
            right= right.next # move right and decrement n. follow loop 
            n -= 1

        # 3. Move left and right pointers one by one, until right reaches to end of LL null
        while right: 
            left = left.next
            right = right. next 
        
        # delete the node in n. delete left.next
        left.next = left.next.next

        # return the new list from dummy, excluding dummy node 
        return dummy.next
        """
        TWO POINTERS AND DUMMY NODE

        1. two pointers: left to head and right to head. 
        2. there should be offset gap between left and right node. that is n gap. 
        3. But left pointer will be in the position, I want to delete. It would be easy if left was in prev of element I wnat to delete. 
        4. to do this, create a dummy node and assign left pointer to it. 

        """
        