class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        
        l = 0
        r = 1

        while (l < r):
            if nums[l] == nums[r]:
                return nums[l]

            else:     
                l += 1
                r += 1
        
        return -1

        