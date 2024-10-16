"""
Two Swaps

Given a permutation of some of the first natural numbers in an array arr[], determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.
"""

class Solution:
    def checkSorted(self, arr):
        n = len(arr)
        swapCnt = 0

        for i in range(n):
            if arr[i] == i + 1:
                continue
            while arr[i] != i + 1:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
                swapCnt += 1

        return swapCnt == 2 or swapCnt == 0
    
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends