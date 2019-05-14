#@Time  : 2019/5/14 16:53
#@Author: Root
#@File  : leetcode28.py


class Solution:
    def strStr(self, t: str, p: str) -> int :
        """
        找到haystack中的needle
        :param haystack:
        :param needle:
        :return:
        """
        if not p: return 0
        _next = [0] * len(p)

        def getNext(p, _next) :
            _next[0] = -1
            i = 0
            j = -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]

        getNext(p, _next)
        i = 0
        j = 0
        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j] :
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(p):
            return i - j
        return -1

    def strStr(self, t, p, n) :
        """
        :param t:
        :param p:
        :param n:
        :return:
        """
        return t.find(p)

string = "123"
string.find("2")
print(Solution().strStr("aaaaaaaa", "aab", 1))