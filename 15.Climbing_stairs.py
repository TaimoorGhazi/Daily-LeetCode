class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def comb(n, r):
            return factorial(n) // (factorial(r) * factorial(n - r))
        
        a = n // 2
        tcomb = 0
        for x in range(0, a + 1):
            v2 = x * 2
            no1 = n - v2
            tchar = no1 + x
            tcomb += comb(tchar, x)
        
        return tcomb


# The fibonnaci approach

# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         f = []
#         f.extend([1, 1])
#         if n <= 1:
#             return f[n]
#         else:
#             for i in range(2, n + 1):
#                 f.append(f[i - 1] + f[i - 2])
#             return f[n]