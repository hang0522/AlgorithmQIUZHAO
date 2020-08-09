class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1:
            return 0
        if not text2:
            return 0
        DP = [[0]*(len(text2)+1) for _ in range(len(text1)+1)] 
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i-1][j-1]+1
                else:
                    DP[i][j] = max(DP[i-1][j],DP[i][j-1])
        return DP[-1][-1]