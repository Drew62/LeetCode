# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, 
# to get accepted, you need to do the following things:
#
#     Change the array nums such that the first k elements of nums contain the elements 
#     which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#     Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notNum = 0
        i = len(nums)-1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            else:
                notNum += 1
            i -= 1
        print(nums, notNum)
        return notNum

solution = Solution()
solution.removeElement([1,2,3,4,5,6,7,8,8,8,9], 8)
