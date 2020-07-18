class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_dic = {}
        for i in range(len(nums)):
            search_num = target-nums[i]
            if search_num in pos_dic:
                return [i, pos_dic[search_num]]
            pos_dic[nums[i]]=i
        return []