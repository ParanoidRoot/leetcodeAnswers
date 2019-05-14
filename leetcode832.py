#@Time  : 2019/4/29 22:15
#@Author: Root
#@File  : leetcode832.py


class Solution:
    def flipAndInvertImage(self, A) :
        return [[(j ^ 1) for j in row][ : : -1] for row in A]
