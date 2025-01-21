class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        ii=0
        target=[]
        for x in range(m+n):
            if i == m:
                target.append(nums2[ii])
                ii+=1
                continue
            if ii == n:
                target.append(nums1[i])
                i+=1
                continue
            if nums1[i] < nums2[ii]:
                target.append(nums1[i])
                i+=1
            else:
                target.append(nums2[ii])
                ii+=1
        nums1[:]=target