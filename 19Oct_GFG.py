"""
Nearest multiple of 10

A string str is given to represent a positive number. 
The task is to round str to the nearest multiple of 10.  
If you have two multiples equally apart from str, choose the smallest element among them.
"""

import sys
class Solution:
    def roundToNearest (self, num_str) :
        sys.set_int_max_str_digits(100000)
        ol = len(num_str)  
    
        num = int(num_str)
        
        lastdigit = num % 10
       
        if lastdigit > 5:  
            rounded_num = num + (10 - lastdigit)  
        else:
            rounded_num = num - lastdigit  
        
        ans = str(rounded_num)  
        nl = len(ans)  
        extraZ = ol - nl
        newans = '0' * extraZ 
        newans += ans
        return newans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends