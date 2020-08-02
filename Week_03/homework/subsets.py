class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        # result = [[]]
        # for num in nums:
        #     result +=[res+[num] for res in result]
        # return result
        result = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums,i):
                result.append(tmp)
        return result