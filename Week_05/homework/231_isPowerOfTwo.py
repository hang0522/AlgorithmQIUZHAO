class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #方法2
        # 若 x 为 2 的幂，则它的二进制表示中只包含一个 1，则有 x & (-x) = x;
        # 若x 不是2 的幂，则它的二进制中不止一个1，则有x &(-x) !=x
        #时间复杂度：O(1)
        #空间复杂度：O(1)
        #if n==0:
        #    return False
        #return n&(-n)==n

        #方法1
        #去除二进制中最右边的 1
        #2 的幂二进制表示只含有一个 1
        #x & (x - 1) 操作会将 2 的幂设置为 0，因此判断是否为 2 的幂是：判断 x & (x - 1) == 0
        if n==0:
            return False
        return n&(n-1)==0