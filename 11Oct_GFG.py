"""
Recognize the array

Given an array of elements arr[] with indices ranging from 0 to arr.size() - 1, your task is to write a program that rearranges the elements of the array such that arr[i] = i. If an element i is not present in the array, -1 should be placed at the corresponding index.
"""

class Solution:
    def rearrange(self, arr):
        rearranged = [-1] * len(arr)

        for num in arr:
            if num != -1 and num < len(arr):
                rearranged[num] = num
    
        return rearranged
        #Code here

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends