#@Time  : 2019/5/26 9:21
#@Author: Root
#@File  : LeetCode32.py

import heapq

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
        :param s:
        :return:
        """
        if not s :
            return 0
        stack = []
        ansQueue = []
        for i, v in enumerate(s) :
            if v == "(" :
                stack.append(i)
            elif len(stack) :
                heapq.heappush(ansQueue, stack.pop())
                heapq.heappush(ansQueue, i)
        if not ansQueue :
            return 0
        table = [0] * len(s)
        last = heapq.heappop(ansQueue)
        table[last] = 1
        while len(ansQueue) :
            current = heapq.heappop(ansQueue)
            if current == last + 1 :
                table[current] = table[last] + 1
            else :
                table[current] = 1
            last = current
        return max(table)

    def better(self, s : str) :
        """
        # 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
        # 考虑动态规划, dp[i] : 表示以i结尾的最长序列的长度
        # if s[i] == "(" 则一定为0
        # if s[i] == ")" and s[i - 1] == "(" => dp[i] = dp[i - 2] + 2
        # if s[i] == ")' and s[i - 1] == ")" and s[i - dp[i - 1] - 1] == "(" 注意动态规划的特性
        # 若dp[i - 1]一定可以找到最长的有效子序列
        #
        :param s:
        :return:
        """
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        dp[0] = 0
        if s[0] == "(" and s[1] == ")" :
            dp[1] = 2
        else :
            dp[1] = 0
        ans = dp[1]
        for i in range(2, len(s)) :
            if s[i] == "(" :
                dp[i] = 0
            elif s[i - 1] == "(" :
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(" :
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]  # 注意新来的右括号使之长度增加后要与之前的相拼接
            ans = max(ans, dp[i])
        return ans



if __name__ == "__main__" :
    print(Solution().better("(()(()((()()(()()(()()(()())(()())"))