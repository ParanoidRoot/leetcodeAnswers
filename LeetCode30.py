#@Time  : 2019/5/14 22:27
#@Author: Root
#@File  : leetcode30.py


class Solution:

    def checkSubstring(self, _p: int, _tempWord2Number: dict, _isVisited: list, _terms: int, _l : int,
                        _s : str, _word2Number : dict):
        """
        子程序 判断从_p开始是否可以构成符合题目的一组解
        :param _p:
        :return:
        """

        i = _p + _l
        while _terms > 0 :
            _currentWord = _s[i: i + _l]
            if _currentWord not in _tempWord2Number.keys():
                while i > _p:
                    _isVisited[i] = True
                    i -= _l
                break
            elif not _tempWord2Number[_currentWord]:  # 个数太少了
                i -= _l
                while i > _p and _tempWord2Number[_currentWord] < _word2Number[_currentWord] :
                    if _s[i : i + _l] == _currentWord :
                        _tempWord2Number[_currentWord] += 1
                        if _tempWord2Number[_currentWord] == _word2Number[_currentWord] :
                            # 找到了最后一个
                                for j in range(i, _p, -_l) :
                                    _isVisited[j] = True
                                break
                    i -= _l
                break
            else:
                _tempWord2Number[_currentWord] -= 1
                _terms -= 1
                i += _l
        return _terms == 0


    def findSubstring(self, s: str, words: list ) -> list :
        """
        给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
        注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
        :param s :
        :param words :
        :return :
        """
        # 注意words可能是有重复的列表
        if not s or not words :
            return []
        t = len(words)
        l = len(words[0])
        n = len(s)
        if n < t * l :
            return []

        word2Number = dict()
        for word in words :
            if word not in word2Number.keys() :
                word2Number[word] = 1
            else :
                word2Number[word] += 1


        ansList = []  # 用于保存最后的答案
        isVisited = [False] * n


        for p in range(0, n - t * l + 1) :
            currentWord = s[p : p + l]
            if not isVisited[p] :
                if currentWord not in word2Number.keys() :
                    isVisited[p] = True
                else :
                    isVisited[p] = True
                    tempWord2Number = word2Number.copy()
                    tempWord2Number[currentWord] -= 1
                    terms = t - 1
                    if self.checkSubstring(
                        _p = p,
                        _isVisited = isVisited,
                        _l = l,
                        _s = s,
                        _tempWord2Number = tempWord2Number,
                        _terms = terms,
                        _word2Number = word2Number
                    ) :
                        ansList.append(p)
        return ansList

if __name__ == "__main__" :
    print(Solution().findSubstring("aabbaabbaabb", ["bb","aa","bb","aa","bb"]))







