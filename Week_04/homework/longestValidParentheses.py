class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        DP = [0]*len(s)
        if len(s)==1:
            return 0
        if len(s)>1:
            DP[0]=0
            for i in range(1,len(s)):
                if s[i] =='(':
                    DP[i] = 0
                if s[i] ==')':
                    if s[i-1] =='(':
                        if (i-2)>=0:
                            DP[i] = DP[i-2]+2
                        else:
                            DP[i] = DP[i-1]+2
                    if s[i-1] ==')':
                        if i-1>=0 and (i-DP[i-1]-1)>=0:
                            if s[i-DP[i-1]-1]=='(':
                                if (i-DP[i-1]-2)>=0:
                                    DP[i] = DP[i-1]+DP[i-DP[i-1]-2]+2
                                else:
                                    DP[i] = DP[i-1]+2
        return max(DP)