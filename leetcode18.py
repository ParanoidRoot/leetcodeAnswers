#@Time  : 2019/5/12 15:46
#@Author: Root
#@File  : leetcode18.p


class Solution:

    def fourSum(self, nums, target) :
        """
        给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
        使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
        注意：
        答案中不可以包含重复的四元组。
        :param nums: list[int]
        :param target: int
        :return: list[list[int] ]
        """
        n = len(nums)
        if n < 4 :
            return []
        ansList = []
        nums.sort()
        p1 = 0
        while p1 < n - 3 :
            if not p1 or nums[p1] != nums[p1 - 1] :
                p2 = p1 + 1
                while p2 < n - 2 :
                    if p2 == p1 + 1 or nums[p2] != nums[p2 - 1] :
                        low = p2 + 1
                        high = n - 1
                        while low < high :
                            currentSum = nums[p1] + nums[p2] + nums[low] + nums[high]
                            lowMoveNeeded = False
                            highMoveNeeded = False
                            if currentSum == target :
                                ansList.append([nums[p1], nums[p2], nums[low], nums[high] ])
                                low += 1
                                high -= 1
                                lowMoveNeeded = True
                                highMoveNeeded = True
                            elif currentSum > target :
                                high -= 1
                                highMoveNeeded = True
                            else :
                                low += 1
                                lowMoveNeeded = True
                            while highMoveNeeded and low < high and nums[high] == nums[high + 1] :
                                high -= 1
                            while lowMoveNeeded and low < high and nums[low] == nums[low - 1] :
                                low += 1
                    p2 += 1
            p1 += 1
        return ansList
