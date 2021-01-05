"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        print('')
        print('inside function...')

        # Declare pointers for traversal. Added for clarity.
        p1 = l1
        p2 = l2

        # Declare current carry over.
        currentCarry = 0

        # Declare cur variable to help traverse and add nodes to new list.
        # Declare head variable to be the head of the list.
        head = cur = ListNode(0)

        # Iteration condition.
        while p1 or p2 or currentCarry:

            print(p1.val, p2.val, currentCarry)

            # Determine current value and carry over.
            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0

            print(currentVal, currentCarry)

            # Add current value as it will always atleast be '1'.
            cur.next = ListNode(currentVal)
            cur = cur.next

            # Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        print('exiting...')
        print('')

        # Return next node.
        return head.next




# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(linked_list_str(l2))

# Add linked lists.
s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(linked_list_str(l3))



######################################################################################################################
# class Node:

#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     # Function to initialize head
#     def __init__(self):
#         self.head = None

#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     # Add contents of two linked lists and return the head
#     # node of resultant list
#     def addTwoLists(self, first, second):
#         prev = None
#         temp = None
#         carry = 0

#         # While both list exists
#         while(first is not None or second is not None):

#             # Calculate the value of next digit in
#             # resultant list
#             # The next digit is sum of following things
#             # (i) Carry
#             # (ii) Next digit of first list (if ther is a
#             # next digit)
#             # (iii) Next digit of second list ( if there
#             # is a next digit)
#             fdata = 0 if first is None else first.data
#             sdata = 0 if second is None else second.data
#             Sum = carry + fdata + sdata

#             # update carry for next calculation
#             carry = 1 if Sum >= 10 else 0

#             # update sum if it is greater than 10
#             Sum = Sum if Sum < 10 else Sum % 10

#             # Create a new node with sum as data
#             temp = Node(Sum)

#             # if this is the first node then set it as head
#             # of resultant list
#             if self.head is None:
#                 self.head = temp
#             else:
#                 prev.next = temp

#             # Set prev for next insertion
#             prev = temp

#             # Move first and second pointers to next nodes
#             if first is not None:
#                 first = first.next
#             if second is not None:
#                 second = second.next

#         if carry > 0:
#             temp.next = Node(carry)

#     # Utility function to print the linked LinkedList
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print temp.data,
#             temp = temp.next


#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#             string1 = ""
#             string2 = ""

#             while l1 is not None:
#                 string1 = str(l1.val) + string1
#                 l1 = l1.next

#             while l2 is not None:
#                 string2 = str(l2.val) + string2
#                 l2 = l2.next

#             sum_strings = int(string1) + int(string2)
#             sum_strings = [int(i) for i in str(sum_strings)]
#             print(sum_strings)

#             head = curr = ListNode(0)

#             for i in range(len(sum_strings)):
#                 while i < len(sum_strings):
#                     curr.next = ListNode(sum_strings[i])
#                     curr = curr.next

#             print(head.next)

# l1 = [2,4,3]
# l2 = [5,6,4]
# s = Solution()
# s.addTwoNumbers(l1, l2)

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def insert(self, root, item):
#         temp = ListNode(0)
#         temp.val = item
#         temp.next = root
#         root = temp
#         return root
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         p1 = l1
#         p2 = l2
#         string1 = ""
#         string2 = ""
#         while p1 is not None:
#             string1 = str(p1.val) + string1
#             p1 = p1.next
#         while p2 is not None:
#             string2 = str(p2.val) + string2
#             p2 = p2.next
#         sum_strings = int(string1) + int(string2)
#         sum_strings = str(sum_strings)
#         sum_strings = [int(i) for i in sum_strings]
#         sum_strings = sum_strings[::-1]
#         root = None
#         for i in range(len(sum_strings)-1, -1, -1):
#             root = self.insert(root, sum_strings[i])
#         return root