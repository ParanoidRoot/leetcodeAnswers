#@Time  : 2019/5/25 21:46
#@Author: Root
#@File  : LeetCode1005.py

import heapq


class Solution:
    def largestSumAfterKNegations(self, A: list, K: int) -> int :
        """
        给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i]
        替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
        以这种方式修改数组后，返回数组可能的最大和。
        :param A:
        :param K:
        :return:
        """
        positiveNumbers = []
        negativeNumbers = []
        for i, v in enumerate(A) :
            if v < 0 :
                heapq.heappush(negativeNumbers, v)
            else :
                heapq.heappush(positiveNumbers, v)
        while K > 0 and len(negativeNumbers) :
            heapq.heappush(positiveNumbers, -1 * heapq.heappop(negativeNumbers))
            K -= 1
        if not K :
            return sum(positiveNumbers) + sum(negativeNumbers)
        else :
            return sum(positiveNumbers) if (not K % 2) else -1 * heapq.heappop(positiveNumbers) + sum(positiveNumbers)





if __name__ == "__main__" :
    Solution().largestSumAfterKNegations([3,-1,0,2,2,3,4,25,31,-2,-3,-4,-44,132], 7)