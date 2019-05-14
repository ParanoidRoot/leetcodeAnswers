#@Time  : 2019/4/29 22:25
#@Author: Root
#@File  : leetcode977.py

class Solution:
    def sortedSquares(self, A) :
        return sorted([a ** 2 for a in A])

    def betterSortedSquares(self, A) :
        """
        如何优化, 平方以及从小打到排序都没有用到这些性质
        :param A:
        :return:
        """
        ansList = []
        left = 0
        right = len(A) - 1
        while left < right :
            l = A[left] ** 2
            r = A[right] ** 2
            if l == r :
                ansList.extend([l, r])
                left += 1
                right -= 1
            elif l < r :
                ansList.append(r)
                right -= 1
            else :
                ansList.append(l)
                left += 1
        if left == right :
            ansList.append(A[left] ** 2)
        return ansList[::-1]
