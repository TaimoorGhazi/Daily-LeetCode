class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        x=-1
        temp=-1
        flag=0
        length=len(haystack)
        needle_length=len(needle)
        if needle in haystack:
            for i in range(length):
                if needle in haystack[i:i+needle_length]:
                    return i
        return x
