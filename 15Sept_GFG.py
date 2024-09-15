"""
Binary to Doubly Linked List

Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. 
The left and right pointers in nodes will be used as previous and next pointers 
respectively in converted DLL. 
The order of nodes in DLL must be the same as the order of the given Binary Tree. 
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.
"""
class Solution:
    def inorder(self, root, node_list):
        """Performs an in-order traversal of the binary tree and stores the nodes in a list."""
        if root is None:
            return
        # Traverse the left subtree
        self.inorder(root.left, node_list)
        # Visit the current node and add it to the list
        node_list.append(root)
        # Traverse the right subtree
        self.inorder(root.right, node_list)

    def bToDLL(self, root):
        """Converts a binary tree to a doubly linked list using in-order traversal."""
        ans = []  # List to hold nodes in in-order sequence
        self.inorder(root, ans)  # Perform in-order traversal and populate ans

        # Edge case: If the tree has no nodes or just one node
        if len(ans) <= 1:
            if ans:  # If there's one node, set its left and right pointers to None
                ans[0].left = ans[0].right = None
            return root

        n = len(ans)  # Number of nodes in the list
        # Loop to link nodes as a doubly linked list
        for i in range(n):
            if i == 0:
                # For the first node, left should be None, and right should point to the next node
                ans[i].left = None
                ans[i].right = ans[i + 1]
            elif i == n - 1:
                # For the last node, right should be None, and left should point to the previous node
                ans[i].right = None
                ans[i].left = ans[i - 1]
            else:
                # For middle nodes, set left to the previous node and right to the next node
                ans[i].left = ans[i - 1]
                ans[i].right = ans[i + 1]

        # Return the head of the doubly linked list, which is the first node in the list
        return ans[0]
    
#{ 
 # Driver Code Starts
#Initial template for Python

from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        head = ob.bToDLL(root)
        printDLL(head)
# } Driver Code Ends
