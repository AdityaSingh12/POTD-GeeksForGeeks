"""
Max_sum_path_in_two_arrays

Given two sorted arrays of distinct integers arr1 and arr2. 
Each array may have some elements in common with the other array. 
Find the maximum sum of a path from the beginning of any array to the end of any array. 
You can switch from one array to another array only at the common elements.

Note:  When we switch from one array to other, 
we need to consider the common element only once in the result.
"""

class Solution:
    def maxPathSum(self, arr1, arr2):
        i, j = 0, 0
        result, sum1, sum2 = 0, 0, 0
        m, n = len(arr1), len(arr2)
        
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1, sum2) + arr1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < m:
            sum1 += arr1[i]
            i += 1

        while j < n:
            sum2 += arr2[j]
            j += 1

        result += max(sum1, sum2)

        return result
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends