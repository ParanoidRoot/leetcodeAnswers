#@Time  : 2019/5/28 21:35
#@Author: ParanoidRoot
#@File  : LeetCode34.py

class Solution:
    def binarySearch4Position(self, nums, target : float, low, high) :
        if low > high :
            return (high, low)
        mid = (low + high) // 2
        if target < nums[mid] :
            return self.binarySearch4Position(nums, target, low, mid - 1)
        elif target > nums[mid] :
            return self.binarySearch4Position(nums, target, mid + 1, high)
        else :
            return mid

    def searchRange(self, nums: list, target: int) :
        """
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
        你的算法时间复杂度必须是 O(log n) 级别。
        如果数组中不存在目标值，返回 [-1, -1]。
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        if not n :
            return [-1, -1]
        if n == 1 :
            if nums[0] == target :
                return [0, 0]
            else :
                return [-1, -1]
        smallerFloatTarget = target - 0.1
        biggerFloatTarget = target + 0.1
        smallerPosition = self.binarySearch4Position(nums, smallerFloatTarget, 0, n - 1)
        if smallerPosition[1] >= n or smallerPosition[1] < 0 or nums[smallerPosition[1]] != target :
            return [-1, -1]
        biggerPosition = self.binarySearch4Position(nums, biggerFloatTarget, smallerPosition[1], n - 1)
        return [smallerPosition[1], biggerPosition[0]] if nums[smallerPosition[1]] == target else [-1, -1]

if __name__ == "__main__" :
    Solution().searchRange([5,7], 8)