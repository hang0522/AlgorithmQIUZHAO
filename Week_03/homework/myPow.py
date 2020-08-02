class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            n = -n
            half =  self.myPow(x,n//2)
            if n%2==0:
              #return 1./(self.myPow(x,n//2)*self.myPow(x,n//2))
              return 1./(half*half)
            else:
              #return 1./(self.myPow(x,n//2)*self.myPow(x,n//2)*x)
              return 1./(half*half*x)
        else:
            half =  self.myPow(x,n//2)

            if n%2==0:
                #return self.myPow(x,n//2)*self.myPow(x,n//2)
                return half*half
            else:
                #return self.myPow(x,n//2)*self.myPow(x,n//2)*x
                return half*half*x