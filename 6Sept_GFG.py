"""
Kadane's Algorithm

Given an integer array arr[]. 
Find the contiguous sub-array(containing at least one number) 
that has the maximum sum and return its sum.
"""

def maxSubArraySum():
    arr=list(map(int, input("Enter any array: ").split()))
    l = len(arr)
    count = arr[0]
    new_count=arr[0]
    
    
    for i in range(1,l):
        count=max(arr[i],count+arr[i])
        new_count=max(new_count, count)
    print(new_count)
maxSubArraySum()