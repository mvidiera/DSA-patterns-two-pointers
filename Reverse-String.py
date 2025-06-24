class Solution(object):
    def reverseString(self, s):
        i=0
        j= len(s)-1

        while(i<j):
            s[i],s[j]= s[j],s[i]

            i+=1
            j-=1
        
        """
        l = 0 
        j = len(s)- 1

        until, i<l, do the following

        swap s[l] with s[r]

        increment i and decrement j
        """