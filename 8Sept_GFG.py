"""
Minimum Jumps

Given an array arr[] of non-negative integers. 
Each array element represents the maximum length of the jumps that can be made forward from that element. 
This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. 
If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.
"""

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1

        for i in range(1, n):
            if i == n - 1:
                return jumps

            maxReach = max(maxReach, i + arr[i])
            steps -= 1

            if steps == 0:
                jumps += 1
                if i >= maxReach:
                    return -1

                steps = maxReach - i
        
        return -1