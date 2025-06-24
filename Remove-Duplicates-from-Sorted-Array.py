class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        j = 1

        for i in range(1,n):
 #nums[1] != nums[0], if its not duplicate, then whatever its in i, put it i (override)            
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1 

            #no else part, as I am doing nothing in else. Just i is incremented in for loop 
        return j
        

"""
2 pointers

i pointer will parse through array to check the unique
j pointer will override the index with newly found element. 

I can point i and j both to index 1 and check as 0th index item will be in result. 

at last return j. 

increment i in for loop
whenever i finds unique element, increment j 

Code:

Variables: i and j is set to 1 index. Element in 0th index is anyway considered for output array

Apply for loop on index i, from i to n 

if i!=j then I found unique item, then i need to shift it where j is that is 1st index. 
once I find unique, then increment j 

else, i == j, then its duplicate. I dont have to do anything. so no else part 
"""
