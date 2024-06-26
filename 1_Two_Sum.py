class Solution(object):
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for a in range(0,len(num)-1):
            for b in range(a+1,len(num)):
                if(num[a]+num[b]==target):
                    ans=[a,b]
                    return ans


sol=Solution()

num=[2,7,11,15]
target=9
ans=sol.twoSum(num,target)
print(ans)
