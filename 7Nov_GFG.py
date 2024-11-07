"""
Split array in three equal sum subarrays

Given an array, arr[], determine if arr can be split into three consecutive parts 
such that the sum of each part is equal. 
If possible, return any index pair(i, j) in an array such that 
sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), 
otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. 
The driver code will print true if it is correct otherwise, it will print false.
"""

class Solution:
    
    def findSplit(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]

        target_sum = total_sum // 3
        current_sum = 0
        first_index, second_index = -1, -1

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == target_sum and first_index == -1:
                first_index = i
            elif current_sum == 2 * target_sum and first_index != -1:
                second_index = i
                break

        if first_index != -1 and second_index != -1:
            last_part_sum = sum(arr[second_index + 1:])
            if last_part_sum == target_sum:
                return [first_index, second_index]

        return [-1, -1]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends