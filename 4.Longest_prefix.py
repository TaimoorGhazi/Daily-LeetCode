class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=''
        if not strs:
            return str
        flag=True
        min_length = min(len(s) for s in strs)
        for x in range(min_length):
            y=strs[0][x]
            for a in range(len(strs)):
                temp=strs[a][x]
                if(y!=temp):
                    flag=False
                    break
            if(flag==True):
                str+=temp
            if(flag==False):
                break                   
        return str