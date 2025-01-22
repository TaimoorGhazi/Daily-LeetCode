class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        target=0
        sqrt = [0,1, 11594, 16379, 20063, 23157, 25869, 28291, 30199, 31703, 33048, 34589, 36040, 37064, 38173, 39233, 46635]
        for i in range(1,17):
            if sqrt[i]*sqrt[i] > x:
                target = sqrt[i-1]
                break
        while 1:
            if target*target > x:
                return target -1
                break
            else:
                target+=1



# This is called Newton's Formula for finding squareroot

#           1/2 ( old guess + x / old guess )

# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ans = x
#         while ans*ans > x:
#             ans = (ans + x//ans)//2
#         return ans 