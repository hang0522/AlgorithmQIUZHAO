class Solution:
    def longestPalindrome(self, s: str) -> str:
        #方法一，循环
        '''
        result = ''
        for i in range(len(s)):
            start = max(0, i - len(result) - 1)
            tmp = s[start: i + 1]
            if tmp == tmp[::-1]:
                result = tmp 
            else:
                if tmp[1:] == tmp[1:][::-1]:
                    result = tmp[1:]
        return result
        '''

        #方法二，动态规划
        result = ''
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = float("-inf")
        for j in range(len(s)):
            for i in range(j + 1):
                if s[j] == s[i] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > max_len:
                    result = s[i: j + 1]
                    max_len = j - i + 1
        print(max_len)
        return result