"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

Constraints:
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""


def findDuplicate(nums):
    d = {}

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)

    duplicates = []
    for k, v in d.items():
        if v > 1:
            duplicates.append(k)

    return duplicates[0]

nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
# nums = [1,1]
# nums = [1,1,2]

print(findDuplicate(nums))

def findDuplicate(nums): # use a set to find duplicates O(1) lookup
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

d = {}
for i in nums:
    if i in d:
        return True
    else:
        d[i] = 1
return False