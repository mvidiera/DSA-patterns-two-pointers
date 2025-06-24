class Solution(object):
    def twoSum(self, numbers, target):
       l = 0 
       r = len(numbers) - 1

       while (l<r):

        res = numbers[l] + numbers[r]

        if res == target: 
            return [l+1, r+1]

        elif res < target: 
            l += 1

        else: 
            r -=1
        

"""
2 pointers: Two sum II has the sorted array 
its also mentioned that numbers is 1 indexed array. It means the index is started with 1, not 0. 

 


1. point l = 0 
2. point r = len(nums)-1 last index 

3. calculate sum which is stored in variable res. 
4. if res is equal to target then, return the indices l and r 
I have to make sure, while returning the indices l and r, I need to add +1 as numbers is 1 indexed array.

5. If the res > target, then I need to reduce my sum, which is done by moving right pointer to left by 1. (decrement)

6. if res < targetm then I need to increase my sum. this is done by moving left pointer to right by 1. (increment)

In question, it has been mentioned that target exists. So no need to return anything if target is not found. 

"""
        