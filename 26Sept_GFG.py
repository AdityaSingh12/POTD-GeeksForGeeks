"""
Roof Top

You are given the heights of consecutive buildings. 
You can move from the roof of a building to the roof of the next adjacent building. 
You need to find the maximum number of consecutive steps you can put forward such 
that you gain an increase in altitude with each step.

"""

class Solution:
    def maxStep(self, arr):
        c = 0  
        m = 0  
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                c += 1  
            else:
                m = max(m, c)  
                c = 0  
        return max(m, c)  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends