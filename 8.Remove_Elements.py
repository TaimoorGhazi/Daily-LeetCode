class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length=len(nums)
        target=[]
        for x in range(length):
            if nums[x] == val:
                target.append(x)
        x=0
        for i in target:
            nums.pop(i-x)
            x+=1
        return (len(nums))