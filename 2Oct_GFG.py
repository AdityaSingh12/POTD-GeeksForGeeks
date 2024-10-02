"""
Rotate & Delete

Given an array arr integers. Assume sz to be the initial size of the array. Do the following operations exactly sz/2 times. In every kth (1<= k <= sz/2) operation:

Right-rotate the array clockwise by 1.
Delete the (n - k + 1)th element from begin.
Now, Return the first element of the array.
Note: Here n keeps on decreasing with every operation.

"""
class Solution:
    def rotateDelete(self, arr):
        n = len(arr)
        k = 1
        while n > 1:
            arr.insert(0, arr.pop())
            id = n - k
            if id < 0:
                id = 0
            arr.pop(id)
            k += 1
            n -= 1
        
        return arr[0]
        


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends

