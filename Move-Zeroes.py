class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 
        r = 0

        for r in range(len(nums)):

            if nums[r] != 0:
                nums[r],nums[l] = nums[l], nums[r]
                
                l += 1

        return nums        

"""
1. L and R points to 0th index
2. L will handle 0 and R will handle non 0 

3. Move R through the array till n 

4. if Rth index is non 0, swap L and R. 
* nums[r] = nums[l]
  nums[l] = nums[r] doesnt work. swapping should be done in single line. 
*  
5. increment l 

6. R will be incremented in for loop
"""