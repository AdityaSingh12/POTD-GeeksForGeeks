"""
You are given an array arr, you need to find any three elements in it such that 
arr[i] < arr[j] < arr[k] and i < j < k.

Note:

The output will be 1 if the subsequence returned by the function is present in the array arr
If the subsequence is not present in the array then return an empty array, the driver code will print 0.
If the subsequence returned by the function is not in the format as mentioned then the output will be -1.
"""


class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        smaller = [-1] * n
        greater = [-1] * n

        min_index = 0
        for i in range(1, n):
            if arr[i] <= arr[min_index]:
                min_index = i
            else:
                smaller[i] = min_index

        max_index = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_index]:
                max_index = i
            else:
                greater[i] = max_index

        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]

        return []


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends