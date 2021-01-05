"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from collections import deque


def twoSum(nums, target):

    dq = deque(sorted([(val, idx) for idx, val in enumerate(nums)])) # sort the values from smallest to greatest

    while True:
        if len(dq) < 2: # if list is less than 2, no answer
            raise ValueError('No match found')

        s =  dq[0][0] + dq[-1][0] # add first and last element of linked list

        if s > target:
            dq.pop() # pops off larger numbers
        elif s < target:
            dq.popleft() # pops off smaller numbers
        else:
            break
    solution =  dq[0], dq[-1] # prints numbers that equal target
    return solution[0][1], solution[1][1] # get indices of the numbers

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))