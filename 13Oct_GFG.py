"""
Delete Alternate Nodes

Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.
"""

#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        while head and head.next:
            head.next = head.next.next
            head = head.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        ob = Solution()
        ob.deleteAlt(head)
        printList(head)

# } Driver Code Ends