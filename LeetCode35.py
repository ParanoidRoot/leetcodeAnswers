#@Time  : 2019/5/28 22:20
#@Author: ParanoidRoot
#@File  : LeetCode35.py


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
        你可以假设数组中无重复元素。
        :param nums:
        :param target:
        :return:
        """
        def binarySearchWithoutReturnNone(nums, target, low, high) :
            if low > high :
                return low
            mid = (low + high) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                return binarySearchWithoutReturnNone(nums, target, low, mid - 1)
            else :
                return binarySearchWithoutReturnNone(nums, target, mid + 1, high)
        return binarySearchWithoutReturnNone(nums, target, 0, len(nums) - 1) if nums else 0