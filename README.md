# DSA-patterns-two-pointers

Two pointers

There are 210 problems in leetcodes, which can be solved using two pointers. 
Brute force solution,  generally uses two for loops. Time complexity will be O(n²), also if any extra space needed then space complexity will be O(n). 
Instead of two for loops, I can use two pointers for the same data structure and use those to compare the elements and find a solution.
Time complexity for array and string is reduced to O(n²) to O(n).


What are two pointers? 
Pointer is a variable that points or represents an index to a position within an array, Linked list. 
If I use linear comparison in data structure, I have to use the nested loop whose time complexity is O(n²). 
To optimize code, I can use 2 points which points two indices within a data structure. 


Types of 2 pointers: 

1. Converging pointers: 
Pointers are initially assigned to two ends of an array. These pointers will be moved towards each other
Based on comparisons, the pointers will be moved. 
These movement of pointers will be stopped when a condition is met or these have crossed each other. 
These techniques of two pointers are used when I need to compare the elements within an array or string. 

Examples: 
Check if the string is pallindrome.
Set the pointer at index  and other pointer at index (n-1)
If these match, move the pointers towards each other. Repeat the process. 
If these do not match, then return False. Not a pallindrome. 


2. Parallel pointers: 

Both pointers will be pointing at 0 th index. Both of these will be moved to single direction. 
The right pointer will move faster, skipping one index so that we have an idea what information lies as we go within an array. 
The left pointer will be at the back, holding all the information. 
This is used in the sliding window.
It is used to check subarrays, to meet specified criteria. 


3. Triggered based pointers: 
In this type, the right pointer will be moved independently based on a condition.
Once the condition is met, the left pointer will move which is used to find more information related to the right pointer. 
This is used when I have to find the information in stages.

Ex: find the nth node from the end of the linked list. 
The right pointer will move till it reaches the nth node. Once it reaches n, the left pointer which is at 0th index will move. 
The movement is such that, both the pointers will move together from their existing positions. 
Each movement will have the same difference in distance, which also can be referred as window. 

R pointer reaches 7, as n= 4, while L will point to 1. 
Once R reaches N and meets condition, both L and R pointer will move until R will reach end. At this point the L pointer will be pointing to N. 

4. Slow and fast pointers: 
Both slow and fast pointers will be pointed to 0th index at first. 
Slow pointer will take one step at a time 
Fast pointer will take 2 steps at a time 

Uses: 
To detect cycles in the linked list: If there is a cycle, the slow and fast pointer will meet at least once. 
To find the middle node: when fast node reaches end, slow node will be pointing to middle node. 



When two pointers are used? 
Used in DS like arrays, strings, Linked list. 
If the DS is following predictable patterns like pallindrome or sorted array. 


Keywords or things to notice in problem, so that I can apply two pointers: 
If the array is sorted. 
If the output needs to return the result of 2 values within the array. 
Find middle
Find a cycle.
If there are 2 arrays and elements have to be compared.











