#@Time  : 2019/5/13 20:21
#@Author: Root
#@File  : leetcode22.py

class Solution:
    def generateParenthesis(self, n) :
        """
        给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
        例如，给出 n = 3，生成结果为：
        :param n : int
        :return : list[str]
        """
        if n <= 0 :
            return [""]
        ansList = []
        currentDecisions = [" "] * (2 * n)
        potentialDecisions = ("(", ")")
        leftBrackets = 0
        rightBrackets = 0
        def backTrack(k) :
            """
            dfs回溯获取ansList
            :param k:
            :return:
            """
            nonlocal leftBrackets
            nonlocal rightBrackets
            if k >= 2 * n :
                ansList.append("".join(currentDecisions))
                return
            for currentDecision in potentialDecisions :
                currentDecisions[k] = currentDecision
                if currentDecision == "(" :
                    leftBrackets += 1
                    if leftBrackets <= n :
                        backTrack(k + 1)
                    leftBrackets -= 1
                else :
                    rightBrackets += 1
                    if rightBrackets <= n and rightBrackets <= leftBrackets :
                        backTrack(k + 1)
                    rightBrackets -= 1
        backTrack(0)
        return ansList

print(Solution().generateParenthesis(2))









