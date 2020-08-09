class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        DP = [[0]*col for _ in range(row)]
        maxSide = 0
        for i in range(row):
            for j in range(col):               
                if matrix[i][j] =='1':
                    if i==0 or j==0:
                        #DP[i][j] =matrix[i][j]
                        DP[i][j] = 1
                        #print("matrix value:",matrix[i][j])
                        #print("DP value:",DP[i][j])
                    else:
                        DP[i][j] = min(DP[i-1][j],DP[i-1][j-1],DP[i][j-1])+1

                    maxSide = max(DP[i][j],maxSide)
        maxArea = maxSide*maxSide
        return maxArea