"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Understand:
    1->2->3, n=1
    1->2

    1->2->3, n=2
    1->3

    1->2->3, n=1
    2->3

    Plan:
    Use dummy head  + two-pointer approach to remove the nth node

    Increment fast point n-times then increment both fast and slow pointers at the same time
    until fast is at the end of the lsit. Once it's at the end of the list
    then slow.next is the node you want to remove
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        dummyHead = ListNode(-1)
        dummyHead.next = head
        left = right = dummyHead
        for i in range(n):
            right = right.next
        while right.next != None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummyHead.next