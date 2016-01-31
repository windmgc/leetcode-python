__author__ = 'windmgc'

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i,j,k = 0,0,0
        m1,m2 = None, None
        m = len(nums1)
        n = len(nums2)
        all = len(nums1) + len(nums2)
        half = all/2
        odd = all%2
        while k < all:
            take = 0
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    take = nums1[i]
                    i = i+1
                else:
                    take = nums2[j]
                    j = j+1
            elif i<m:
                take = nums1[i]
                i = i+1
            else:
                take = nums2[j]
                j = j+1
            k = k+1
            if odd == 1:
                if k > half:
                    m1 = take
                    return m1
            else:
                if k >= half:
                    if m1 == None:
                        m1 = take
                    else:
                        m2 = take
                        return float(m1+m2)/2.0