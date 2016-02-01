__author__ = 'windmgc'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        result = 0
        if x >=0:
            flag = 1
        else:
            flag = 0
            x = -x
        while x!=0:
            result += x % 10
            x = x // 10
            result *= 10
        result = result / 10
        if flag == 0:
            result = -result
        if result > 2 ** 31 - 1 or result < -2 ** 31 :
            return 0
        else:
            return result