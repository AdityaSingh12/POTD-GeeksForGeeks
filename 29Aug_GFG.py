"""
Find Length of loop


Given the head of a linked list, determine whether the list contains a loop. If a loop is present, 
return the number of nodes in the loop, otherwise return 0.

Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist.
If c is 0, then there is no loop.
"""

class Solution:
    class ListNode:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def countNodesInLoop(self, head):
        # Initialize pointers
        slow = head
        fast = head
        
        # Step 1: Detect the loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Loop detected
                return self.countLoopLength(slow)
        
        # If no loop is found
        return 0
    
    def countLoopLength(self, loop_node):
        # Start from the node where slow and fast met
        temp = loop_node
        count = 1
        while temp.next != loop_node:
            count += 1
            temp = temp.next
        return count
    

#Driver code starts
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        index += 2

"""