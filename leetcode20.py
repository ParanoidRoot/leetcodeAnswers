#@Time  : 2019/5/12 16:36
#@Author: Root
#@File  : leetcode20.py


class Solution:
    def isValid(self, s) :
        """
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串
        :param s: str
        :return: bool
        """
        if not s :
            return True
        if len(s) % 2 == 1 :
            return False
        m = {
            "(" : -3, ")" : 3,
            "[" : -2, "]" : 2,
            "{" : -1, "}" : 1
        }
        stack = []
        for t in s :
            if m[t] < 0 :
                stack.append(m[t])
            elif not len(stack) or stack.pop() != -m[t] :
                    return False
        return not len(stack)

    def somethingAwesome(self, s) :
        """
        令人惊艳的做法但是同时效率不如上面一种，适合装逼
        :return:
        """
        while "{}" in s or "[]" in s or "()" in s :
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""
