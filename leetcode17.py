#@Time  : 2019/5/12 15:16
#@Author: Root
#@File  : leetcode17.py

class Solution:

    telephoneKeyboard = {
        "2" : ("a", "b", "c"),
        "3" : ("d", "e", "f"),
        "4" : ("g", "h", "i"),
        "5" : ("j", "k", "l"),
        "6" : ("m", "n", "o"),
        "7" : ("p", "q", "r", "s"),
        "8" : ("t", "u", "v"),
        "9" : ("w", "x", "y", "z")
    }

    def letterCombinations(self, digits: str) :
        """
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        :param digits:
        :return:
        """
        if digits == "" :
            return []
        currentDecisions = list(" " * len(digits))
        ansList = []
        m = self.telephoneKeyboard
        def backTrack(k) :
            """
            回溯法获取答案
            :param k:
            :return:
            """
            if k >= len(digits) :
                ansList.append("".join(currentDecisions))
                return
            potentialDecisions = m[digits[k]]
            for currentDecision in potentialDecisions :
                currentDecisions[k] = currentDecision
                backTrack(k + 1)
        backTrack(0)
        return ansList

Solution().letterCombinations("23")



