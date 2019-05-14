#@Time  : 2019/5/14 16:46
#@Author: Root
#@File  : leetcode27.py


class Solution:
    def removeElement(self, nums, val) :
        """
        删除数组nums中的所有为val的元素
        :param nums:
        :param val:
        :return:
        """
        if not nums :
            return 0
        p = 0
        while p < len(nums) :
            if nums[p] == val :
                nums.pop(p)
            else :
                p += 1
        return len(nums)
