class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        方法1
        a = list(s)
        for i in range(0,len(s),2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)