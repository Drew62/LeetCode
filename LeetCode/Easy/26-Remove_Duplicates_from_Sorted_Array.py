# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#     Change the array nums such that the first k elements of nums contain the unique elements
#     in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#     Return k.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # When removing from an array the size will change, but if we iterate backwords 
        # we dont have to worry about that constrant
        i = len(nums) - 1 # start at last index
        while i >= 0: # while the index does not equal 0 
            val = nums[i] 
            if i-1 >= 0: # If the next index is not negative/not a valid index in the array
                nextVal = nums[i-1]
                if val == nextVal:
                    nums.pop(i) # remove the duplicate
            i -= 1 # iterate backwords
        
        return len(nums)
        
solution = Solution()
solution.removeDuplicates([1,1,2])
