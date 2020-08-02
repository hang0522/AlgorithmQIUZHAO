class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <1:
            return []
        self.result =[]
        self.pie = []
        self.na = []
        self.cols=[]
        self.helper(0,n,[])
        return self._generator(n)

    def helper(self,level,n,cur):
        #terminator
        if level==n:
            self.result.append(cur)
        #process
        for col in range(n):
            if col in self.cols or level+col in self.pie or level-col in self.na:
                continue
            self.cols.append(col)
            self.pie.append(level+col)
            self.na.append(level-col)
            #cur.append([col])
            #cur = cur+[col]
            #drill down
            self.helper(level+1,n,cur+[col])
            
            #reverse
            self.cols.remove(col)
            self.pie.remove(level+col)
            self.na.remove(level-col)
    def _generator(self,n):
        self.output =[]
        tmp_result = []
        for res in self.result:
            for idx in res:
                self.output.append('.'*idx + 'Q'+'.'*(n-idx-1))
        for tmp in range(0,len(self.output),n):
            tmp_result.append(self.output[tmp:tmp+n])
        return tmp_result
        # return [self.output[i:i+n] for i in range(0,len(self.output),n)]