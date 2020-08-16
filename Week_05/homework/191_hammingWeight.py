class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt =0
        while n:
          cnt+=n&1
          n = n>>1
        return cnt
        ###1#####
        #x=x&(x-1) and count
        # res = 0
        # while n!=0:
        #     res+=1
        #     n&=n-1 #set last bit as 0
        #     print (n)
        # return res
        
        ###2#####
        #res = bin(n).count("1")
        #return res