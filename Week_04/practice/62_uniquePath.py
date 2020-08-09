class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # #print(dp) [[1, 1], [1, 0], [1, 0]]
        # #dp1 = [[1]*n] #print(dp1)# [[1, 1]]
        # # dp2 = [[1]+[0]*(n-1)for _ in range(m-1)] #print(dp2)  [[1, 0], [1, 0]]
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # return dp[-1][-1]
        # cur = [[1]*n]
        # pre = [[1]*n]
        cur = [1]*n
        #pre = [1]*n
       
       
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cur[j] = pre[j] + cur[j-1]
        #     print(cur)
        #     pre = cur[:]
        # return pre[-1]

        
        for i in range(1,m):
            #print("cur:",cur)
           # print("pre:",pre)
            for j in range(1,n):
               # cur[j] = pre[j]+cur[j-1]
               cur[j]+=cur[j-1]
            #print("after cur:",cur)
            #pre = cur
        return cur[-1]