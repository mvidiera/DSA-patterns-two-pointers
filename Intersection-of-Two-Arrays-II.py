class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while( i < len(nums1) and j < len(nums2)):

            if nums1[i] == nums2[j]:

                res.append(nums1[i])
                i += 1
                j += 1
            
            elif nums1[i] < nums2[j]:
                i += 1
            
            else:
                j += 1

        return res


"""
2 pointers:

nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Sort the arrays first.

nums1 = [4,5,9]
nums2 = [4,4,8,9,9]

i pointer will point to 0th index of nums1
j poiner will point to 0th index of nums2

if i == j, then append it in res array. 
i ++ and j++ 

increment the pointer which has less number: 

if i< j, then i++

if i > j, then j++

this is because, i or j, if it has less element than other there is a chance of finding a match, as the arr is sorted. 

stop the while loop when either i or j reach out of bound. 

return res
"""