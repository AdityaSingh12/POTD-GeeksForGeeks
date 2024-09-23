"""
Missing and Repeating

Given an unsorted array arr of of positive integers. 
One number 'A' from set {1, 2,....,n} is missing and one number 'B' occurs twice in array. Find numbers A and B.
"""
class Solution:
    def findTwoElement(self, arr): 
        n = len(arr)
        xor_all = 0
        xor1 = 0
        xor2 = 0

        for i in range(n):
            xor_all ^= arr[i]     
            xor_all ^= (i + 1)    

        set_bit = xor_all & ~(xor_all - 1)

        for i in range(n):
            if (arr[i] & set_bit) != 0:  
                xor1 ^= arr[i]
            else:                        
                xor2 ^= arr[i]

            if ((i + 1) & set_bit) != 0:  
                xor1 ^= (i + 1)
            else:                         
                xor2 ^= (i + 1)

        repeating, missing = 0, 0
        for i in range(n):
            if arr[i] == xor1:
                repeating = xor1
                missing = xor2
                break
            elif arr[i] == xor2:
                repeating = xor2
                missing = xor1
                break

        return [repeating, missing]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends