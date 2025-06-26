class Solution(object):
    def checkInclusion(self, s1, s2):
        n1= len(s1)
        n2= len(s2)

# 1st condition is to check n1> n2. if greater, n1 is obviously not substring of n2
        if n1>n2:
            return False

        # frequency array for s1 and s2 and set it 0 and which has 26 representing 26 alphabets
        # index from 0 to 25

        s1_counts= [0]*26
        s2_counts= [0]*26

        # create initial frequency counter, s1 is fixed. 
        # suppose s1= bc, then ord(b)= 98, 98-97 (b has index 1, whereas a has index 0)
        # s1_counts= [0,1,0,0,...]
        # bc: c-> 99-97= 2 index-> s1_counts = [0,1,1,0,0.... 0] last index is 25 which belongs to z
        for i in range(n1): 
            s1_counts[ord(s1[i]) - 97] += 1 # ord('a') ascii is 97 
            s2_counts[ord(s2[i])- 97] += 1
        
        # check it counts matches
        if s1_counts == s2_counts:
            return True
        
        # SLIDING WINDOW 
        for i in range(n1, n2): # n1= window size and s2 where I am sliding the window of size n1
            # move right-> add the character to right. s1= bc s2= abcd. 1st window was checked in prev for
            # win = bc: lose 'a' and add 'c'
            s2_counts[ord(s2[i]) - 97 ] += 1
            # lose the character from left
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1 # exp at last

            if s1_counts == s2_counts:
                return True 
        
        return False

# why s2[i-n1] -> here i= 2 (range n1)and n1= 2
# I need to lose the 1st character whose index is 0. 2-2= 0 
# ex: gain "c" and lose "a"
# s2_counts(ord(c)- 97) = 2-> [0,1,1....]
#s2_counts(ord(a)- 97 ) = 0 -> make index 0 as 0. 
            
        
        