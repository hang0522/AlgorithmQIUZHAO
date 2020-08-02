class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        
        #此处不能用双重for循环
        # for i in range(len(g)):
        #   for j in range(len(s)):
        #     if s[j]>=g[i]:
        #       s[j]=0
        #       count+=1
        g= sorted(g)
        s = sorted(s)
        i,j = 0,0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count