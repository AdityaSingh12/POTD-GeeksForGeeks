"""
Construct Binary Tree from Parent Array

Given an array parent that is used to represent a tree. The array indices (0-based indexing) are the values of the tree nodes and parent[i] denotes the parent node of a particular node. The parent of the root node would always be -1, as there is no parent for the root. Construct the standard linked representation of Binary Tree from this array representation and return the root node of the constructed tree.

Note: If two elements have the same parent, the one that appears first in the array will be the left child and the other is the right child. You don't need to print anything, the driver code will print the level order traversal of the returned root node to verify the output.
"""

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        if n <= 0 or head is None:
            return 0

        fast = head
        slow = head

        for _ in range(n):
            if fast is None:
                return 0
            fast = fast.next

        sum_last_n = 0

        while fast is not None:
            fast = fast.next
            slow = slow.next

        while slow is not None:
            sum_last_n += slow.data
            slow = slow.next

        return sum_last_n