class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket=""
        target=""
        for x in range(len(s)):
            if s[x] not in bucket:
                bucket=bucket+s[x]
            else:
                if len(bucket) >= len(target) :
                    target=bucket
                i=bucket.find(s[x])
                bucket=bucket[i+1:]+s[x]
        if not target or len(bucket) >= len(target):
            target = bucket
        return len(target)







