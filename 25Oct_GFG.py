"""
Alternative Sorting

Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and the second element is the smallest, the third element is the second largest and the fourth element is the second smallest, and so on.
"""

class Solution:
    def alternateSort(self, arr):
        arr.sort()  
        n = len(arr)
        ans = []
        
        left, right = 0, n - 1
        highTurn = True
        
        for _ in range(n):
            if highTurn:
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1
            highTurn = not highTurn
        
        return ans