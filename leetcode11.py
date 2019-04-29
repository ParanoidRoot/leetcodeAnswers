#@Time  : 2019/4/30 7:27
#@Author: Root
#@File  : leetcode11.py


class Solution:
    def maxArea(self, height) -> int :
        """
        返回最大的蓄水池容积，贪心算法
        :param height:
        :return:
        """
        l = 0
        h = len(height) - 1
        maxAns = 0
        while l < h :
            maxAns = max(maxAns, min(height[l], height[h]) * (h - l))
            if height[l] < height[h] :
                l += 1
            else :
                h -= 1
        return maxAns