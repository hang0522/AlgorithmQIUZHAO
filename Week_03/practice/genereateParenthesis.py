class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #judge if valid
        if n==0:
          return []
        left_cnt = 0
        right_cnt = 0
        self.result = []
        self.helper(left_cnt,right_cnt,'',0,n)
        return self.result
    def helper(self,left_cnt,right_cnt,cur,idx,n):
        #terminator
        if idx==2*n:
            self.result.append(cur)
            return
        #process data
        if left_cnt<n:
            self.helper(left_cnt+1,right_cnt,cur+'(',idx+1,n)
        if left_cnt>right_cnt and right_cnt<n:
            self.helper(left_cnt,right_cnt+1,cur+')',idx+1,n)