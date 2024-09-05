"""
Given an array arr of size n-1 that contains distinct integers in the range of 1 to n (inclusive), 
find the missing element.
The array is a permutation of size n with one element missing. Return the missing element.
"""

class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        x=[]
        c=0
        d=0
        for i in range(1,n+1):
            x.append(i)
            c=c+i
        for j in range(0,n-1):
            d=d+arr[j]
        return c-d


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)