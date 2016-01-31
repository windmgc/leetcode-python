__author__ = 'windmgc'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        another_index=0
        for i,x in enumerate(nums):
            if nums.count(target-x) == 0:
                pass
            elif target/2 == x:
                for j,y in enumerate(nums):
                    if y == x:
                        if j == i:
                            pass
                        else:
                            another_index = j
                            if i < another_index:
                                return [i+1, another_index+1]
                            else:
                                return [another_index+1, i+1]
            else:
                another_index = nums.index(target-x)
                if i < another_index:
                    return [i+1, another_index+1]
                else:
                    return [another_index+1, i+1]

    def twoSum2(self, nums, target):
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x] + 1, i + 1]
            index[x] = i







