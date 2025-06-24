class Solution(object):
    def strStr(self, haystack, needle):

        m = len(needle)
        n = len(haystack)
        
        # I have to go through haysack, so take for loop on n

        for i in range(n):
            j = 0

            for k in range(i, n): # move k in inner loop

                if haystack[k] == needle[j]:
                    j += 1 # move needle and k will be incremented in inner loop 

#if not matching reset, then break inner loop k. i++, j=0, k=0

                else:
                    break
                
                if j == m: 
                    return i 
        
        return -1 




"""
2 pointers on Haysack
1 pointer at needle. 

idea: i and k points to haysack 
j -> needle

if k = j, move both k and j 
else
increment i, i and k will start with same index
and j be on 0th index

when to stop:
if j and k are same and reaches end of len(needle)


Code: 
variables: 2 pointer i and k for Haystack. 
i to return the 1st pointer and k to compare with needle 

needle has one pointer k 

loops: 2 for loop 

outer loop: for i 

inner loop: k -> to check if k ==j, 
if k == j, then increment j and k will be any way incremented in inner loop

if k != j, then break k loop.

Now outer loop, i will increment. 
i = 1, k and j will be reset to 0 

else: return -1 as no needle is found in haystack
"""
        