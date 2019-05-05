#@Time  : 2019/5/5 16:42
#@Author: Root
#@File  : leetcode15.py


class Solution :

    def getKeyStr(self, a) :
        """
        返回特征关键字
        :param a:
        :return:
        """
        return "_".join([str(n) for n in a])


    def threeWrongSum(self, nums) :
        """
        找出元素为0的列表集合
        :param nums:
        :return:
        """
        if len(nums) < 3 :
            return []
        nums.sort()
        numbers = nums
        dictionary = {
            numbers[0] + numbers[1] : [ [ numbers[0], numbers[1] ] ]
        }
        myMap = {self.getKeyStr(numbers[0 : 2])}
        ansList = []
        p = 2
        while p < len(numbers) :
            currentNumber = numbers[p]
            owedNumber = -currentNumber
            if owedNumber in dictionary.keys() :
                tempAnsList = dictionary[owedNumber]
                for tempAns in tempAnsList :
                    tempAns.append(currentNumber)
                    ansList.append(tempAns)
                dictionary[owedNumber] = None
                del dictionary[owedNumber]
            for i in range(0, p) :
                a = [numbers[i], numbers[p]]
                keyStr = self.getKeyStr(a)
                if keyStr not in myMap :
                    #这种组合没遇见过
                    myMap.add(keyStr)
                    aSum = sum(a)
                    if aSum in dictionary.keys() :
                        dictionary[aSum].append(a)
                    else :
                        dictionary[aSum] = [a]
            p += 1
        return ansList

    def threeSum(self, numbers) :
        """
        返回numbers中三数为0的子序列
        :param numbers:
        :return:
        """
        if len(numbers) < 3 :
            return []
        numbers.sort()
        ansList = []
        p = 0
        while p < len(numbers) - 2 :
            if p == 0 or numbers[p] > numbers[p - 1] :
                currentNumber = numbers[p]
                owedNumber = -currentNumber
                low = p + 1
                high = len(numbers) - 1
                while low < high :
                    lowMoveNeeded = False
                    highMoveNeeded = False
                    tempSum = numbers[low] + numbers[high]
                    if tempSum == owedNumber :
                        ansList.append([currentNumber, numbers[low], numbers[high]])
                        lowMoveNeeded = True
                        low += 1
                        highMoveNeeded = True
                        high -= 1
                    elif tempSum > owedNumber :
                        highMoveNeeded = True
                        high -= 1
                    else :
                        lowMoveNeeded = True
                        low += 1
                    while lowMoveNeeded and numbers[low] == numbers[low - 1] and low < high :
                        low += 1
                    while highMoveNeeded and numbers[high] == numbers[high + 1] and low < high :
                        high -= 1
            p += 1
        return ansList








if __name__ == "__main__" :

    numbers = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(numbers))








