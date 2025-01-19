class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        for x in range(length):
            if target == nums[x] or target < nums[x]:
                return x
        return length

# class Solution(object):
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """

    #     for i in range(len(nums)):
    #         if nums[i]>target or nums[i]==target:
    #             return i
    #     return len(nums)
        