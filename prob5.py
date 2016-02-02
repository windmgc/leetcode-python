__author__ = 'windmgc'

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_string = ""
        for i in xrange(len(s)):
            present_length = 0
            left_pointer = i
            right_pointer = i
            while left_pointer >=0 and right_pointer <= len(s)-1:
                if s[left_pointer] == s[right_pointer]:
                    print left_pointer,right_pointer
                    present_length = (i - left_pointer) * 2 + 1
                    if present_length >= len(max_string):
                        max_string = s[left_pointer:right_pointer+1]
                        print max_string
                    left_pointer -= 1
                    right_pointer += 1

        return max_string
