"""
Nth Natural Number

Given a positive integer n. 
You have to find nth natural number after removing all the numbers containing the digit 9.
"""

class Solution:
    def findNth(self, n):
        # Convert n to base-9 and interpret it as a decimal number
        result = 0
        base = 1
        
        while n > 0:
            result += (n % 9) * base
            n //= 9
            base *= 10
        
        return result

# Example usage
sol = Solution()
n = int(input("Enter the value of n: "))
print(f"The {n}th natural number after removing numbers containing digit 9 is: {sol.findNth(n)}")
