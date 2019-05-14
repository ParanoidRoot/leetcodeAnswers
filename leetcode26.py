#@Time  : 2019/5/14 16:38
#@Author: Root
#@File  : leetcode26.py


class Solution:
    def removeDuplicates(self, nums) :
        """
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        :param nums :
        :return :
        """
        if not nums :
            return 0
        p = 1
        while p < len(nums) :
            if nums[p] == nums[p - 1] :
                nums.pop(p)
            else :
                p += 1
        return len(nums)

