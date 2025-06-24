class Solution(object):
    def maxArea(self, height):
        res= 0
        left= 0
        right= len(height)-1

        while(left < right):
            area= (right-left) * min(height[left], height[right])
            res= max(res, area)

            if height[left] < height[right]:
                left += 1
            #elif height[left] > height[right]:
            #    right -= 1
            else:
                right -= 1 #can eliminate 2 lines as else case: we can either move left or right. I decided to move right so eliminating elif
        return res

"""
Variables used: 
1. area: calculated area using height x breadth. res= 0. 
2. res: holds maximun value of area 
3. point l to 0th index, r to len(height) - 1

4. while loop is used, loop is stopped when the left pointer will be more than right. 
5. Each while loop calculate area
6. once area is calculated, compare this with the max of res. 

As this approach uses 2 pointers. 
Pointer 1 (L) will point to index 0, R will point to (n-1)
area = will have the area, Height x breadth(distance btw 2 pointers)

Breadth = distance btw 2 pointers will be (R - L )

while loop, until left pointer surpasses right.
calculate area = HEIGHT: take min bwt 2 pointers, as it holds water. 
BREADTH= (right - left)

res will hold maximum of all areas

Now its time to move the pointers: 
check which point is less, increment/decrement pointer which is less 

As the pointers are in left and right. left pointer will be incremented and right pointer will be decremented. 

if height[l] < height[r] then move left. else decrement right

"""
            
        