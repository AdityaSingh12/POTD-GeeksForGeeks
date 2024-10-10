"""
Max distance between same elements

Given an array arr[] with repeated elements, 
the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.
"""

class Solution:
    def maxDistance(self, arr):
        mp = {}
        max_dist = 0
        for i in range(len(arr)):
            if arr[i] not in mp:
                mp[arr[i]] = i
            else:
                max_dist = max(max_dist, i - mp[arr[i]])

        return max_dist

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends