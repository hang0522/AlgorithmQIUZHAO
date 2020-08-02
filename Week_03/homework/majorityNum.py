class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        idx = int(len(nums)/2)
        return nums[idx]