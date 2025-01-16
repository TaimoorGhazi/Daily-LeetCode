class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vars=0
        varm=0
        varl=0
        list=[-1]
        for x in range(len(s)):
            if(s[x]=='('):
                vars-=1
                list.append(0)
            if(s[x]==')'):
                vars+=1
                a=list.pop()
                if(a is not 0):
                    return False
            if(s[x]=='{'):
                varm-=1
                list.append(1)
            if(s[x]=='}'):
                varm+=1
                a=list.pop()
                if(a is not 1):
                    return False
            if(s[x]=='['):
                varl-=1
                list.append(2)
            if(s[x]==']'):
                varl+=1
                a=list.pop()
                if(a is not 2):
                    return False
        if vars is 0 and varm is 0 and varl is 0:
            return True
        else:
            return False