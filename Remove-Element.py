class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #n = len(nums)

        l = 0 
        r = len(nums)

        while (l<r):
            # if I find val, then replace it 
            if nums[l] == val:
                nums[l] = nums[r-1]

                r -= 1

            else: 
                l += 1
        
        return r



"""
val-> element I need to remove from array.

return number of elements I am keeping after deleting the duplicates.

2 pointers: 

l -> index 0 
r-> index (n-1)

when l finds 2 (which is supposed to be delete), remove this from l and replace it with the item r pointer has. 

* when l != val. l++
when l = val, replace it with r and then r-- 


In beginning, I have considered r as len(nums)- 1 and when the while loop breaks, l= 5 and r = 4. 

As I have subtracted by 1 to fit into last index, while returning I have to make sure that I need to add +1. 

hence, return r+1. 

Other way is to consider, r= len(nums) -> nums[l] = nums[r-1] -> return r

this doesn't work for the test case: [1]
l, r both points to 1. 
val = 1

is l == val? yes, replace it with r. even r is has same and single value. 
r = -1. l = 0, break while loop. 

but op = [1], whereas it should be []. 

better to use r= len(nums) -> nums[l] = nums[r-1] -> return r
"""