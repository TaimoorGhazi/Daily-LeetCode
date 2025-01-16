class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list=[]
        x=0
        while x<len(s):
                if s[x]=="M":
                    list.append(1000)
                if s[x]=="D":
                    list.append(500)
                if s[x]=="C":
                    if((x+1)<len(s) and s[x+1]=="D"):
                        list.append(400)
                        x=x+1
                    elif((x+1)<len(s) and s[x+1]=="M"):
                        list.append(900)
                        x=x+1    
                    else:
                        list.append(100)
                if s[x]=="L":
                    list.append(50)
                if s[x]=="X":
                    if((x+1)<len(s) and s[x+1]=="L"):
                        list.append(40)
                        x=x+1
                    elif((x+1)<len(s) and s[x+1]=="C"):
                        list.append(90)
                        x=x+1
                    else:
                       list.append(10)
                if s[x]=="V":
                    list.append(5)
                if s[x]=="I":
                    if((x+1)<len(s) and s[x+1]=="V"):
                        list.append(4)
                        x=x+1
                    elif((x+1)<len(s) and s[x+1]=="X"):
                        list.append(9)
                        x=x+1
                    else:
                        list.append(1)
                x=x+1
        return sum(list)


