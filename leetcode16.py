#@Time  : 2019/5/12 14:30
#@Author: Root
#@File  : leetcode16.py

import sys


class Solution:
    def threeSumClosest(self, nums, target = 0) :
        """
        获取与target最接近的三数之和
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 3 :
            return 0
        minDelta = sys.maxsize
        ans = 0
        nums.sort()
        p = 0
        while p < len(nums) - 2 :
            low = p + 1
            high = len(nums) - 1
            while low < high :
                currentDelta = nums[p] + nums[low] + nums[high] - target
                if not currentDelta :
                    return target
                else :
                    if abs(currentDelta) < minDelta :
                        minDelta = abs(currentDelta)
                        ans = currentDelta + target
                    lowMoveNeeded = (currentDelta < 0)
                    highMoveNeeded = (currentDelta > 0)
                    if lowMoveNeeded :
                        low += 1
                    if highMoveNeeded :
                        high -= 1
                    while lowMoveNeeded and low < high and nums[low] == nums[low - 1] :
                        low += 1
                    while highMoveNeeded and low < high and nums[high] == nums[high + 1] :
                        high -= 1
            p += 1
        return ans


