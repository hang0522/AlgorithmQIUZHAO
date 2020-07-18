class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k:
            #solution 1:
            #nums[:k],nums[k:] = nums[-k:],nums[:-k]
            #solution 2:
            nums[:] = nums[-k:]+nums[:-k]