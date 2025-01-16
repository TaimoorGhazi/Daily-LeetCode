class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list=[]
        temp=x
        while(temp>0):
            list.append(temp%10)
            temp=temp//10
        if x<0:
            return False
        mid=len(list)/2
        flag=True
        for x in range(mid):
            if( list [x] != list [-(x+1)]):
                flag=False
        if flag==True:
            return True
        else:
            return False