class Solution:
    def countSubstrings(self, s: str) -> int:

        n= len(s)
        res = 0

        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):

                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]= True 
                    res= res+1
        return res


  
  
"""
1. n-> len(s)
2. res to hold number of pallindromes
3. dp 2D array which holds T or F. (initally all set to false)

4. Outer loop i: starts from last char in str, till 1st char and go left one by one
5. Inner loop j : ranges from i till n (excluding n )

ex: aaab 

i = 3
j = 3 till 3 (1 char substring)

is s[i]==s[j]? yes. j-1<=2? yes. res++
"b" is taken 
res= 1
just one loop inner, so exit from inner loop. 

i = 2
j = 2 till 3 (2 loops)

i = a j= a (3rd char)
is s[i]==s[j]? yes. j-1<=2? yes. res++
"a" is taken
res= 2

aaab
j= 3
i = a j= b (2 char)
is s[i]==s[j]?-> no 

done with inner loop j, come out of loop. 

aaab 
i = 1
j = 1 2 3

i = 1
j = 1
i = a j= a (2nd a)
is s[i]==s[j]? yes. j-1<=2? yes. res++
"a" is taken
res= 3

j = 2
i = a j = a -> aa
is s[i]==s[j]? yes. j-1<=2? yes. res++
"aa" is taken
res= 4

j = 3
i = a j = b -> (ab)
is s[i]==s[j]?-> no. 
done with inner loop., come out of j loop 

i = 0 
j = 0 1 2 3

i = 0, j = 0 (a)
is s[i]==s[j]? yes. j-1<=2? yes. res++
"a" is taken
res= 5

i = 0 j= 1 (aa)
is s[i]==s[j]? yes. j-1<=2? yes. res++
"a" is taken
res= 6

i = 0 j = 2 (aaa)
is s[i]==s[j]? yes. j-1<=2? yes.
dp[i+1][j-1] = dp[1][1]= True  res++
"aaa" is taken
res= 7

i = 0 j = 3 (aaab)
is s[i]==s[j]? no, done with inner loop, come out of j loop 

"""