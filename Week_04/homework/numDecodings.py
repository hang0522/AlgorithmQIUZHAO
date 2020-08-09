class Solution:
    def numDecodings(self, s: str) -> int:
        if not len(s):
            return 0
        if s[0] =='0':
            return 0
        DP = [0]*len(s)
        DP[0] = 1
        if len(s)>1:
            if s[1]=='0':
                if int(s[0:2])>26:
                    return 0
                else:
                    DP[1] = 1
            else:
                if int(s[0:2])>26:
                    DP[1] = 1
                else:
                    DP[1] = 2
        else:
            return 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i-1] =='0':
                    return 0
                else:
                    if int(s[i-1:i+1])>26:
                        return 0
                    else:
                        DP[i] = DP[i-2]
            else:
                if s[i-1]=='0':
                    DP[i] = DP[i-1]
                else:
                    if int(s[i-1:i+1])>26:
                            DP[i] = DP[i-1]
                    else:
                        DP[i] = DP[i-1]+DP[i-2]
        return DP[-1]