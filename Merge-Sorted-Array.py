class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

# 3 pointers. m end of x, n end of y and z-> end of x's garbage. 
#loop goes backwards. 
# among x and y, whichever the highest override that with z. (in garbage 0)
# and decrement tht pointer which was moved. 

        x = m - 1
        y = n - 1

        for z in range( (m + n - 1), -1, -1): 

            if x < 0: # ex: x[], y= [1 2 3], copy everythin on y  to z(which is end of x)
                nums1[z] = nums2[y]
                y -= 1

            elif y < 0:
                break
            
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]

                x -= 1
            
            else: 
                nums1[z] = nums2[y]
                y -= 1
            
#Do not return anything, modify nums1 in-place instead.        
        
        
        
"""
refer ipad notes
"""
        