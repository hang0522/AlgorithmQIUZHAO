class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        counter = collections.Counter(s)
        for idx,s in enumerate(s):
            if counter[s]==1:
                return idx
        return -1