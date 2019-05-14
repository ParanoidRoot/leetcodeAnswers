#@Time  : 2019/5/14 21:38
#@Author: Root
#@File  : leetcode29.py


class Solution:
    def divide(self, dividend: int, divisor: int) -> int :
        """
        给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
        返回被除数 dividend 除以除数 divisor 得到的商。
        :param dividend :
        :param divisor :
        :return :
        """
        if not dividend :
            return 0
        if dividend == -2147483648 and divisor == -1 :
            return 2147483647
        isNegative = (dividend ^ divisor) < 0  # 判断正负号
        tempDividend = abs(dividend)
        tempDivisor = abs(divisor)
        ans = 0
        for rightMoveDigits in range(31, -1, -1) :  # 判断第一个最大的2的幂次，能够使得与divisor相乘后任然小与当前的被除数
            if (int(tempDividend) >> int(rightMoveDigits)) >= tempDivisor :
                ans += 1 << int(rightMoveDigits)
                tempDividend -= int(tempDivisor) << int(rightMoveDigits)
        return ans if not isNegative else -ans

    """
    比如
    被除数是100，除数是3
    3 * 32 = 96 所以ans += 2^5; 同时剩余被除数 := 100 - 96 = 4
    3 * 1 =3 所以 ans += 1; 同时剩余被除数 := 4 - 3 = 1
    """
