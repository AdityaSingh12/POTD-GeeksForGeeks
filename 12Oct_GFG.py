"""
Two Smallests in Every Subarray

Given an array of integers arr, the task is to find and return the maximum sum of the smallest and second smallest element among all possible subarrays of size greater than one. If it is not possible, then return -1.
"""

class Solution:
    def pairWithMaxSum(self, arr):
        n=len(arr)
        ans=0
        for i in range(1,n):
            ans=max(ans,arr[i]+arr[i-1])
        return ans if ans else -1
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends
