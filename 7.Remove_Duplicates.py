class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list=[]
        r=[]
        for x in range(len(nums)):
            if nums[x] in list:
                r.append(x)
                continue
            list.append(nums[x])
        x=0
        for i in r:
            nums.pop(i-x)
            x+=1
        return len(list)
        


# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0  
        
#         unique_index = 0  
        
#         for i in range(1, len(nums)):
#             if nums[i] != nums[unique_index]:
#                 unique_index += 1
#                 nums[unique_index] = nums[i]
        
#         return unique_index + 1 