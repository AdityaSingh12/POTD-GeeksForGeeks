"""
Middle of Linked List

Given the head of a linked list, the task is to find the middle. 
For example, the middle of 1-> 2->3->4->5 is 3. If there are two middle nodes (even count), 
return the second middle. 
For example, middle of 1->2->3->4->5->6 is 4.
"""

class Solution:
    def findMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow.data