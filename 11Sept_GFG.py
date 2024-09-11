"""
Minimum Costs of Rope

Given an array arr containing the lengths of the different ropes, 
we need to connect these ropes to form one rope. 
The cost to connect two ropes is equal to sum of their lengths. 
The task is to connect the ropes with minimum cost.  
"""

from typing import List
import heapq

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        # If there's only one or no rope, no cost is needed.
        if len(arr) <= 1:
            return 0
        
        # Convert the list into a min-heap.
        heapq.heapify(arr)
        total_cost = 0

        # Continue until only one rope remains.
        while len(arr) > 1:
            # Pop the two smallest elements (ropes) from the heap.
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Connect the ropes (sum them) and add to the total cost.
            cost = first + second
            total_cost += cost
            
            # Push the combined rope back into the heap.
            heapq.heappush(arr, cost)
        
        return total_cost