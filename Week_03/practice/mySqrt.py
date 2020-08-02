class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        left = 1 
        right = x
        while left<=right:
            #print((right-left)//2)
            mid = int(left + (right-left)/2)
            #print("mid =",mid)
            #mid = left + (right - left + 1) // 2
            #mid = (left + right + 1) >> 1
            square = mid * mid
            if square>x:
                right = mid-1
            else:
                left = mid+1
                #left = mid
        return int(right)