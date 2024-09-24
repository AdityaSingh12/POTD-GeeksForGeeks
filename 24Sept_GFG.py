"""
Smallest window in a string containg all the characters of another string

Given two strings s and p. Find the smallest window in 
the string s consisting of all the characters(including duplicates) of the string p. 
Return "-1" in case there is no such window present. 
In case there are multiple such windows of same length, 
return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 
"""

class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"

        phash = [0] * 256
        for ch in p:
            phash[ord(ch)] += 1

        shash = [0] * 256
        minLength = float('inf')
        startIndex = -1
        count = 0
        left = 0

        for right in range(len(s)):
            ch = s[right]
            shash[ord(ch)] += 1

            if phash[ord(ch)] != 0 and shash[ord(ch)] <= phash[ord(ch)]:
                count += 1

            while count == len(p):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    startIndex = left
                
                leftChar = s[left]
                shash[ord(leftChar)] -= 1

                if phash[ord(leftChar)] != 0 and shash[ord(leftChar)] < phash[ord(leftChar)]:
                    count -= 1
                
                left += 1  

        if startIndex == -1:
            return "-1"
        return s[startIndex:startIndex + minLength]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends