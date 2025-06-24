class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans= ""
        count = -1

        n= len(s)

        dp = [[False]*n for _ in range(n)]

        for g in range(n): #g= substring len
            for i in range(n-g): # left index ends in substring len

                j = i+g # right index

                #base cases i= 0, j= 0 (1 character)
                if g==0: 
                    dp[i][j] = True # all diagonal cells are T as single char is pallindrome by itself

                elif g==1: #i= 0, j= 1 (2 characters)
                    dp[i][j] = (s[i] == s[j])
                
                else: #update dp for i and j where g>=3
                    dp[i][j] = (s[i]== s[j] and dp[i+1][j-1])
                
                # check if this is longest
                if dp[i][j] and count<j-i+1: # i=0 j=2 g=3 ex: bab
                    ans = s[i:j+1]
                    count= len(ans)
        
        return ans
        


"""
1. variables needed. ans = str t return the longest substring 
count: it keeps count of each pallindrome and then return the largest one. if I found largest now and in next iteration, 
length reduces, count wont be updated. 
n-> len of inpout string 

2. create a 2D array dp of size n*n and set each elemet to false. 
2D array-> 2 bracker [[]] of size n: *n. for loop in range(n)
dp = [[false]* n for _ in range(n)]

3. 2 for loop 

outer for: g which is length of substring. range(n) : 0 to n-1

inner for: i  (1st or left index which points to start of substring)
this ranges from 0 to n-g
why (n-g)?
ex: aababa
n= 5, I need substring 3
if I start from 0th index, len should be ended at 2nd index. 0 1 2
so n-g: 5-3= 2. i starts with 0 and end with 2. ( 0 1 2)

Base cases: 
a. when g=0, i = j= 0 that means I need just one length substring: Diagonally all are 1 or True

b. when g=1, i=0, j=1. 2 length substring. 
check if s[i]==s[j] is true then its Pal, else not 

else: 
(check notes)
2 conditoons have to be satisfied to update dp
a. outer characters should be same AND
b. inner characters, check its dp[i+1][j-1], i is incremented and j is decremented

Now it is time to check the length of palindrome
in 1st iteration: count = -1
now g=2 i= 0 j= 1
ex: aa
if (dp[i][j] and count< j-i+1 (outer index - inner index +1)
ans = s[i: j+1] : s[0:2] excluding 2
ans = aa
count = len(aa) = 2

next loop 

count = 2. g=3. 
i=0 j= n-g = 5-3= 2 
j= 2
(0,1,2)

ex: bab
if(dp[i][j] and count < j-i+1) True and (2<2-0+1= 3) (is 2<3) True
both condition satisfies so update answer
ans= bab



""" 