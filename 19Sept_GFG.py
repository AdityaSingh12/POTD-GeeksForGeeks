"""
Given a String str, reverse the string without reversing its individual words. 
Words are separated by dots.

Note: The last character has not been '.'. 
"""

class Solution:
    def reverseWords(self,str):
        words = str.split('.')  
        reversed_words = words[::-1]  
        reversed_string = '.'.join(reversed_words)  
        return reversed_string

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends