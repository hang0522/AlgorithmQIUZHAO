class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res +=((n&1)<<power)
            n = n>>1
            power -=1
        return res

##################
#C++ version
# class Solution {
# public:
#     uint32_t reverseBits(uint32_t n) {
#         int res =0;
#         for(int i=0;i<=31;i++)
#         {
#             res^= (n&(1<<i)) !=0?1<<(31-i):0;
#         }
#         return res;
#     }
# };