"""
Facing the Sun

Given an array height representing the heights of buildings. 
You have to count the buildings that will see the sunrise 
(Assume the sun rises on the side of the array starting point).
Note: The height of the building should be strictly greater 
than the height of the buildings left in order to see the sun.
"""

class Solution:
    def countBuildings(self, height):
        count=1
        x=height[0]
        for i in range(1,len(height)):
            if x<height[i]:
                count= count+1
                x=height[i]
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends