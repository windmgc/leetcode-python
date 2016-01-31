__author__ = 'windmgc'

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        length = 1
        if s == "":
            return 0
        else:
            while right < (len(s)-1):
                if s[left:right+1].find(s[right+1]) != -1:
                    left += s[left:right+1].find(s[right+1]) + 1
                else:
                    right += 1
                    if length <= (right - left):
                        length = right - left + 1
            return length






