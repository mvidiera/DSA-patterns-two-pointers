# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
2 pointer
"""
class Solution(object):
    def reorderList(self, head):
        """
        Part A: find middle. 
        1. using slow and fast pointer.
        2. once fast pointer reaches the end of list. slow.next will be considered as second part of the list. 

        Part B: Reverse second part
        1. Before reversing, make end of 1st part as None as it will be end of list. 
        2. using temp and 2 pointers as in reverse LL, reverse the list.  

        Part C: Merge 2 lists: by breaking the existing link and arranging 
        1. 2 pointers, 2 temp variables. 
        2. 2 parts of list can be same size. 2nd part can be shorter than 1st. But, 1st pointer can never be shorter than second.

        while loop

        3. I want (1)-> (4). 1 is head and 4 here is prev. it was reversed, now it is (4)->(3)
        4. assign ptr1= head and ptr2= prev. (1st ele after reversing)
        5. store the next items of these 2 pointers in temp variables. 
        6. 
        7. Move pointers first and second


        """
        #part A: find middle

        slow= head
        fast= head.next 

        while fast and fast.next: #till there is fast and fast.next elements are there
            slow= slow.next
            fast= fast.next.next 

        #assign middle/ second part 
        second = slow.next 

        # Part B: Reversing second part: 
        slow.next= None
        prev= None
        # I need 2 pointers to reverse: curr and prev. here curr is second and prev

        while second: 
            tmp= second.next
            second.next = prev
            prev= second
            second= tmp

        # Part C: merging
        # needs 2 tmp variables to store head and prev. 
        first= head
        second= prev

        while second: 
            tmp1= first.next 
            tmp2 = second.next

            first.next= second
            second.next= tmp1

            # update or move pointers to right
            first= tmp1
            second= tmp2

        

        