class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()

        count = 0
        left= 0
        right= len(nums)-1

        while(left< right):
            if(nums[left] + nums[right] < target):
                count += right-left #why? as the array is sorted, left from 2 are less that 2 or 2 itself. the combination between -1 and 1 or 2 will be less than 2. hence taking count= count + right - left. 
                left += 1
        
            else:
                right -= 1
        
        return count
        
"""
[-6,2,5,-2,-7,-1,3] taget = -2

sort [-7 -6 -2 -1 2 3 5]

l points to 0 and r points to len(nums)-1

-7 + 5 = -2. is less than -2. no then move r to left 

-7-3 = -4. is less than -2? yes. 

now I found the sum which is less than target and I can say that which ever left of 3, every sum with -7 will be less than 2. 

How to find the number of elements between right and left pointer?
right - left. 
5- 0 = 5 

count = 0 
count = count + 5 - 0. 5. 
l ++

[-7 -6 -2 -1 2 3 5]
l -> -6 r-> 5 

-6+5 no r --
-6+3 yes and everything before 3 is counted

count = 5 + 5 - 1
count = 9 
l++

[-7 -6 -2 -1 2 3 5]
l -> -2 r-> 5 (6)
r-3. as I have moved r thrice. r = 
-2+5 no, -2+3 no, -2+2 no. -2-1 yes. 
r= 3. 

count = 9 + 3 - 2
count = 10  
 l ++

[-7 -6 -2 -1 2 3 5]
l -> -1 
r -> 5 

-1+5, no r--. 
-1 +3, no r--
-1 + 2 no. r-- no 

return count

""" 