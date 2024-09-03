"""
Given two strings str1 and str2. 
The task is to remove or insert the minimum number of characters from/in 
str1 so as to transform it into str2. It could be possible that the same 
character needs to be removed/deleted from one point of str1 and inserted to some another point.
"""
class Solution:
    def minOperations(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if str1[i - 1] == str2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return m + n - 2 * dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)
