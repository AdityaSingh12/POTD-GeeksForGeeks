"""
Modify the Array

Given an array arr. Return the modified array in such a way that if the current and next numbers are valid numbers and are equal then double the current number value and replace the next number with 0. After the modification, rearrange the array such that all 0's are shifted to the end.

Note:

Assume ‘0’ as the invalid number and all others as a valid number.
The sequence of the valid numbers is present in the same order.
"""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)

        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] = 2 * arr[i]
                arr[i + 1] = 0

        nonZeroIndex = 0
        for i in range(n):
            if arr[i] != 0:
                arr[nonZeroIndex] = arr[i]
                nonZeroIndex += 1

        while nonZeroIndex < n:
            arr[nonZeroIndex] = 0
            nonZeroIndex += 1

        return arr


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends