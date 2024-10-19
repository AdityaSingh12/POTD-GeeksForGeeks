"""
Single Number

Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.
"""

 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        result = 0
        for num in arr:
            result ^= num
        return result


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends