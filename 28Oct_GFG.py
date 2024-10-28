"""
Remove duplicates in array

Given an array arr consisting of positive integer numbers, remove all duplicate numbers.
"""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        x=[]
        for i in range(0,len(arr)):
            if arr[i] not in x:
                x.append(arr[i])
                
        return x
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends