class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i,j = 0,0
        for num in bills:
            if num==5:
              i+=1
            if num==10:
              j+=1
              i-=1
            if num==20:
              if j>0:
                j-=1
                i-=1
              else:
                i-=3
            if i<0:
                return False
        return True