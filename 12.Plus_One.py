class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        edit=1
        edited =[1]
        zero=[0]
        for x in range(1,len(digits)+1):
            if digits[-x]==9:
                digits[-x]=0
                edit+=1
            else:
                break
        if edit == len(digits)+1:
            return edited+digits
        else:
            digits[-edit]+=1
        return digits