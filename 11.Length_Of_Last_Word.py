class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        flag=0
        for x in range(1,(len(s)+1)):
            if s[-x] == " " and flag == 0:
                continue
            if s[-x] == " ":
                break
            else:
                flag =1
                count+=1
                continue
        return count