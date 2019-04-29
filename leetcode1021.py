#@Time  : 2019/4/29 21:29
#@Author: Root
#@File  : leetcode1021.py


class Solution :
    def removeOuterParentheses(self, S: str) -> str :
        """
        实现有效字符串的分割与拼接
        :param S:
        :return:
        """
        ansList = []
        s = []
        index = 0
        while index < len(S) :
            p = S[index]
            if p == "(" :
                s.append(index)
            else :
                l = s.pop()
                if len(s) == 0 :
                    ansList.append((l, index))
            index += 1
        ansStr = "".join([S[fromIndex + 1 : toIndex ] for fromIndex, toIndex in ansList])
        return ansStr

S = "(()())(())"

print(Solution().removeOuterParentheses(S))