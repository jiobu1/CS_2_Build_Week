"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.


"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeTwoSorted(self, l1, l2):
        p1 = l1
        p2 = l2

        newList = ListNode(0)

        while p1 or p2:
            if p1.val < p2.val:
                #  append p2 to p1
                newList.next = p1
                p1 = p1.next

            else:
                # append p1 to p2
                newList.next = p2
                p2 = p2.next

            if p1 is None and p2 is None:
                break
            elif p1 is  None:
                newList.next = p2.val
                p2 = p2.next
            elif p2 is None:
                newList.next = p1.val
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        return newList


sol = Solution()
l1 = [1,2,4]
l2 = [1,3,4]
sol.mergeTwoSorted(l1, l2)