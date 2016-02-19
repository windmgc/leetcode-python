__author__ = 'windmgc'

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result_str = ""
        if numRows == 1:
            return s
        else:
            rows = [""] * numRows
            turn, at_row = -1, 0
            for i in s:
                rows[at_row] += i
                if at_row == 0 or at_row == numRows - 1:
                    turn *= -1
                at_row += turn

        for i in rows:
            result_str += i

        return result_str
