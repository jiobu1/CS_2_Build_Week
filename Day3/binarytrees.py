"""
Binary Trees: Review

            balanced  | unbalanced
get     | O(n)        | O(logn)
insert  | O(n)        | O(logn)
remove  | O(n)        | O(logn)

n will be number of nodes
always clarify assumptions

in order for it to be a complete binary tree, nodes need to be to the left
complete binary trees are also balanced


Traversals
Depth-First
In-order
    left -> right
    left -> current -> right
    sorted order
Reverse-in-oder
    right -> current -> left
Pre-order
    before
    process root before children
    root -> left -> right
Reverse-pre-order
    process root -> right -> left
Post-order
    process children before root
    left -> right -> root
Reverse-pre-order
    right -> left -> root
Keywords: need to reach out to the deepest, max, longest

Breadth-First Search(BFS)
queue
keywords: level, row, closest, minimum, width, diameter

Problem
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000


Understand
Example
Root = [3]
Ouput: 1

Plan:
Use BFS to find closet shallow leaf. Keep track of the current level of teh node.
Once you encounter a leaf, output its level
"""

from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==  None:
            return 0
        queue = deque()
        queue.append((root, 1))
        while len(queue) > 0:
            curr = queue.popleft()
            currNode, currLevel = curr[0], curr[1]

            if currNode.left == None and currNode.right == None:
                return currLevel
            if currNode.left != None:
                queue.append((currNode.left, currLevel + 1))
            if currNode.right != None:
                queue.append((currNode.right, currLevel + 1))
        return -1

root = [3,9,20,null,null,15,7]
s = Solution()
s.minDepth(root)